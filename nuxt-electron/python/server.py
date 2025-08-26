import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # для локальной разработки
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_text()
        print(f"Received from client: {data}")
        await ws.send_text(f"Echo: {data}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)