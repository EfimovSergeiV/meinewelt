from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket</title>
    </head>
    <body>
        <h1>WebSocket</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("wss://api.meinewelt.ru/chat");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)

from datetime import datetime


messages = []
clients = []

@app.websocket("/chat")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    # сразу отправляем текущую историю
    await websocket.send_json({"connection_id": id(websocket)})
    await websocket.send_json(messages)

    try:
        while True:
            data = await websocket.receive_text()
            new_message = {
                "client_id": id(websocket),
                "text": data,
                "time": datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            }
            messages.append(new_message)
            if len(messages) > 5:
                messages.pop(0)

            # рассылаем всем клиентам
            for client in clients:
                await client.send_json(new_message)
    except:
        clients.remove(websocket)



from data import gen_datasets, floating_list_make
import json

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(f"Message text was:{data}")

        # Переводим запрос в JSON
        json_data = json.loads(data)

        if json_data["chart"] in ["bar", "bubble", "multiline"]:
            response_data = gen_datasets(json_data["chart"])

        if json_data["chart"] == "watch":
            response_data = floating_list_make()

        await websocket.send_json(response_data)


"""
    TEST LLM AGENT WITH FASTAPI AND WEBSOCKETS
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import lmstudio as lms
import re, random, json, asyncio
from pathlib import Path

SERVER_API_HOST = "192.168.1.123:1234"
lms.configure_default_client(SERVER_API_HOST)
model = lms.llm("openai/gpt-oss-20b")

REPLACEMENTS_FILE = Path("replacements.json")


SYSTEM_PROMPT = ("""

    EXAMPLE PROMT:

""")


# =========================
# HELPERS
# =========================
def log(msg: str):
    print(msg, flush=True)


def load_replacements() -> dict:
    """
    Загружает словарь замен из JSON.
    """
    if not REPLACEMENTS_FILE.exists():
        return {}

    try:
        with open(REPLACEMENTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        return {str(k).lower(): str(v) for k, v in data.items()}
    except Exception as e:
        log(f"[WARN] Не удалось загрузить replacements.json: {e}")
        return {}
    

def preserve_case(original: str, replacement: str) -> str:
    """
    Сохраняет регистр оригинального слова:
    человек -> чел
    Человек -> Чел
    ЧЕЛОВЕК -> ЧЕЛ
    """
    if original.isupper():
        return replacement.upper()
    elif original[:1].isupper():
        return replacement.capitalize()
    return replacement


def replace_words(text: str, replacements: dict) -> str:
    """
    Заменяет слова по словарю только по границам слов.
    """
    if not replacements:
        return text

    pattern = r"\b(" + "|".join(map(re.escape, replacements.keys())) + r")\b"

    def repl(match):
        original = match.group(0)
        replacement = replacements.get(original.lower(), original)
        return preserve_case(original, replacement)

    return re.sub(pattern, repl, text, flags=re.IGNORECASE)


def naturalize_бля(text: str) -> str:
    """
    Делает речь более живой и слегка ебанутой, но не слишком.
    """
    result = []

    # for ch in text:
    #     if ch == ".":
    #         if random.random() < 0.15:
    #             result.append(" бля")
    #         result.append(".")
    #     elif ch == "!":
    #         if random.random() < 0.10:
    #             result.append(" бля")
    #         result.append("!")
    #     elif ch == "?":
    #         if random.random() < 0.10:
    #             result.append(" бля")
    #         result.append("?")
    #     else:
    #         result.append(ch)

    # text = "".join(result)

    # text = re.sub(
    #     r"\b(ну|короче|слушай|вообще|просто)\b",
    #     lambda m: m.group(1) + (" бля" if random.random() < 0.4 else ""),
    #     text,
    #     flags=re.IGNORECASE
    # )

    # text = re.sub(r"\s{2,}", " ", text)
    return text


class FinalStreamExtractor:
    """
    На лету вытаскивает только содержимое final-ответа из потока модели.
    """

    def __init__(self):
        self.raw = ""
        self.in_final = False
        self.output_pos = 0

    def feed(self, chunk: str) -> str:
        self.raw += chunk

        if not self.in_final:
            marker = "<|channel|>final<|message|>"
            idx = self.raw.find(marker)
            if idx == -1:
                return ""
            self.in_final = True
            self.output_pos = idx + len(marker)

        visible = self.raw[self.output_pos:]

        stop_markers = [
            "<|end|>",
            "<|start|>",
            "<|channel|>",
            "<|message|>",
        ]
        cut_positions = [visible.find(m) for m in stop_markers if visible.find(m) != -1]
        if cut_positions:
            visible = visible[:min(cut_positions)]

        visible = re.sub(r"<\|.*?\|>", "", visible)

        already_printed = self.raw[self.output_pos:self.output_pos + len(visible)]
        self.output_pos += len(already_printed)

        return visible


# =========================
# CLIENT CHAT SESSIONS
# =========================
class ChatSession:
    def __init__(self):
        self.chat = lms.Chat(SYSTEM_PROMPT)
        self.lock = asyncio.Lock()


# на каждый websocket-клиент будет своя сессия
# если хочешь потом хранить по user_id/token — можно вынести отдельно
sessions = {}


# =========================
# WEBSOCKET
# =========================
@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    client_id = id(websocket)

    session = ChatSession()
    sessions[client_id] = session

    log(f"[WS] Client connected: {client_id}")

    try:
        while True:
            user_input = await websocket.receive_text()
            user_input = user_input.strip()

            if not user_input:
                await websocket.send_json({
                    "type": "error",
                    "content": "Пустой запрос"
                })
                continue

            log(f"[WS] {client_id} -> {user_input!r}")

            async with session.lock:
                replacements = load_replacements()

                # Добавляем юзерское сообщение в чат
                session.chat.add_user_message(user_input)

                # Стрим от модели
                prediction_stream = model.respond_stream(
                    session.chat,
                    on_message=session.chat.append,
                )

                extractor = FinalStreamExtractor()
                pending = ""
                full_answer = ""

                try:
                    for fragment in prediction_stream:
                        chunk = fragment.content or ""
                        if not chunk:
                            continue

                        clean_piece = extractor.feed(chunk)
                        if not clean_piece:
                            continue

                        pending += clean_piece

                        # Отдаём только на естественной границе
                        split_matches = list(re.finditer(r"[.,!?]\s+|\n", pending))
                        if split_matches:
                            last_end = split_matches[-1].end()
                            to_send = pending[:last_end]
                            pending = pending[last_end:]

                            to_send = replace_words(to_send, replacements)
                            to_send = naturalize_бля(to_send)

                            full_answer += to_send

                            await websocket.send_json({
                                "type": "chunk",
                                "content": to_send
                            })

                            # маленькая уступка event loop, чтобы не залипало
                            await asyncio.sleep(0)

                    # Хвост
                    if pending.strip():
                        pending = replace_words(pending, replacements)
                        pending = naturalize_бля(pending)
                        full_answer += pending

                        await websocket.send_json({
                            "type": "chunk",
                            "content": pending
                        })

                    await websocket.send_json({
                        "type": "done",
                        "content": full_answer
                    })

                    log(f"[WS] {client_id} <- done ({len(full_answer)} chars)")

                except Exception as e:
                    log(f"[ERR] Stream error for {client_id}: {e}")
                    await websocket.send_json({
                        "type": "error",
                        "content": f"Ошибка генерации: {str(e)}"
                    })

    except WebSocketDisconnect:
        log(f"[WS] Client disconnected: {client_id}")

    except Exception as e:
        log(f"[ERR] WebSocket fatal error {client_id}: {e}")

    finally:
        sessions.pop(client_id, None)





