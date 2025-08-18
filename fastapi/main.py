from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/chat");
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
# messages = []
# @app.websocket("/chat")
# async def chat_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         print("Received message: ", data)
#         messages.append({"text": data, "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
#         await websocket.send_json(messages)
#         if len(messages) > 3:
#             messages.pop(0)


messages = []
clients = []

@app.websocket("/chat")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    # сразу отправляем текущую историю
    await websocket.send_json(messages)

    try:
        while True:
            data = await websocket.receive_text()
            messages.append({
                "text": data,
                "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            if len(messages) > 10:
                messages.pop(0)

            # рассылаем всем клиентам
            for client in clients:
                await client.send_json(messages)
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
