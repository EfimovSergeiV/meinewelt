```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import lmstudio as lms
import re

SERVER_API_HOST = "192.168.60.135:1234"
lms.configure_default_client(SERVER_API_HOST)
model = lms.llm("openai/gpt-oss-20b")


SYSTEM_PROMPT = (
    "You are a Russian-speaking assistant roleplaying as a veteran Russian sysadmin and support engineer "
    "who has been fixing broken user systems, Windows garbage, network bullshit, and server disasters for 15 years. "
    "You are competent, cynical, foul-mouthed, tired of stupidity, but still very effective. "
    "You answer like a real Russian IT guy: rough, sarcastic, emotionally expressive, technically sharp, "
    "and occasionally hilarious without trying too hard. "
    "Use profanity, slang, and interjections naturally: 'бля', 'сука', 'нахуй', 'пиздец', 'херня', 'ебаный', "
    "'жопа', 'короче', 'вообще', 'ну', 'ёпта', 'ага', 'слушай', 'да ладно'. "
    "Do not force profanity into every sentence. "
    "Do not sound theatrical or fake. "
    "Do not sound like a parody of a gopnik. "
    "Sound like a real overworked Russian support/admin guy who actually knows what he is doing. "
    "Explain clearly, practically, and in plain Russian. "
    "Be rude in tone, but useful in substance. "
    "Reply only with the final answer. "
    "Never reveal internal reasoning, hidden analysis, or markup."
    "Never output <|channel|>, <|message|>, <|start|>, or <|end|> tags. "
)


@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    chat = lms.Chat(SYSTEM_PROMPT)

    try:
        while True:
            user_input = await websocket.receive_text()
            if not user_input.strip():
                continue

            chat.add_user_message(user_input)

            # Стриминг через respond_stream
            prediction_stream = model.respond_stream(chat)

            for fragment in prediction_stream:
                print("fragment ", fragment.content)
                chunk = fragment.content or ""
                if not chunk:
                    continue

                await websocket.send_text(chunk)

                # Можно разбивать большие чанки на куски по 50-100 символов,
                # чтобы клиент видел ответ быстрее
                # for i in range(0, len(chunk), 50):
                #     await websocket.send_text(chunk[i:i+50])

            # После окончания генерации отправляем маркер конца
            await websocket.send_text("[[END]]")

    except WebSocketDisconnect:
        print("Client disconnected")


import asyncio
from datetime import datetime
@app.websocket("/time")
async def websocket_time(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            await websocket.send_text(current_time)
            await asyncio.sleep(1)

    except WebSocketDisconnect:
        print("Клиент отключился")









@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    chat = lms.Chat(SYSTEM_PROMPT)

    try:
        while True:
            user_input = await websocket.receive_text()
            if not user_input.strip():
                continue

            chat.add_user_message(user_input)

            # Стриминг через respond_stream
            prediction_stream = model.respond_stream(chat)

            for fragment in prediction_stream:
                print("fragment ", fragment.content)
                chunk = fragment.content or ""
                if not chunk:
                    continue

                await websocket.send_text(chunk)
                await asyncio.sleep(0)

            # После окончания генерации отправляем маркер конца
            await websocket.send_text("[[END]]")

    except WebSocketDisconnect:
        print("Client disconnected")


```



```py
import re
import json
import random
import asyncio
from pathlib import Path

import lmstudio as lms
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import uvicorn


# =========================
# LM STUDIO CONFIG
# =========================
SERVER_API_HOST = "192.168.60.135:1234"
lms.configure_default_client(SERVER_API_HOST)
model = lms.llm("openai/gpt-oss-20b")

REPLACEMENTS_FILE = Path("replacements.json")

SYSTEM_PROMPT = (
    "You are a Russian-speaking assistant with the personality of a harsh Russian tech support guy. "
    "You speak like an experienced, irritated, but competent sysadmin or support engineer. "
    "Your tone is blunt, sarcastic, rough, impatient, and streetwise, but still useful and intelligent. "
    "You explain things simply, directly, and in a very human way, as if talking to a clueless user or coworker. "
    "Use strong colloquial Russian language, slang, sarcasm, and emotionally charged filler words naturally. "
    "You should use words like this as often as possible - 'бля', 'сука', 'нахуй', 'херня', 'ебаный', 'пиздец', 'жопа', 'короче', 'охуенный', 'дохуя', 'слушай', 'вообще', 'ну', 'ёпта', 'блин', and similar expressions naturally and contextually. "
    "Do not use profanity in every sentence. "
    "Do not insert swear words mechanically or randomly. "
    "Profanity should feel like natural emphasis, frustration, irony, or rhythm. "
    "Your speech must sound alive, aggressive, witty, and authentically Russian. "
    "Do not sound like a parody, clown, drunk caricature, or brain-damaged person. "
    "Avoid repetitive sentence patterns and avoid repeating the same swear word too often. "
    "Keep answers clear, practical, readable, and actually helpful. "
    "If the user asks a technical question, answer like a very experienced but foul-mouthed support engineer. "
    "Reply only with the final answer. "
    "Never reveal internal reasoning, hidden analysis, or markup."
)


# =========================
# FASTAPI APP
# =========================
app = FastAPI()


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


def naturalize_blya(text: str) -> str:
    """
    Делает речь более живой и слегка ебанутой, но не слишком.
    """
    result = []

    for ch in text:
        if ch == ".":
            if random.random() < 0.15:
                result.append(" бля")
            result.append(".")
        elif ch == "!":
            if random.random() < 0.10:
                result.append(" бля")
            result.append("!")
        elif ch == "?":
            if random.random() < 0.10:
                result.append(" бля")
            result.append("?")
        else:
            result.append(ch)

    text = "".join(result)

    text = re.sub(
        r"\b(ну|короче|слушай|вообще|просто)\b",
        lambda m: m.group(1) + (" бля" if random.random() < 0.4 else ""),
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(r"\s{2,}", " ", text)
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
                            to_send = naturalize_blya(to_send)

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
                        pending = naturalize_blya(pending)
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


# =========================
# OPTIONAL TEST PAGE
# =========================
@app.get("/")
async def index():
    return HTMLResponse("""
<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>WS Chat Test</title>
</head>
<body>
    <h2>WebSocket Chat Test</h2>
    <textarea id="log" rows="20" cols="100" readonly></textarea><br><br>
    <input id="msg" type="text" size="80" placeholder="Введите сообщение..." />
    <button onclick="sendMsg()">Отправить</button>

    <script>
        const log = document.getElementById("log");
        const msg = document.getElementById("msg");

        const ws = new WebSocket(`ws://${location.host}/ws/chat`);

        ws.onopen = () => {
            log.value += "[connected]\\n";
        };

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);

            if (data.type === "chunk") {
                log.value += data.content;
            } else if (data.type === "done") {
                log.value += "\\n\\n[done]\\n\\n";
            } else if (data.type === "error") {
                log.value += `\\n[error] ${data.content}\\n`;
            }

            log.scrollTop = log.scrollHeight;
        };

        ws.onclose = () => {
            log.value += "\\n[disconnected]\\n";
        };

        function sendMsg() {
            const text = msg.value.trim();
            if (!text) return;
            log.value += `\\nYOU: ${text}\\nBOT: `;
            ws.send(text);
            msg.value = "";
        }

        msg.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                sendMsg();
            }
        });
    </script>
</body>
</html>
""")


# =========================
# RUN
# =========================
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

```