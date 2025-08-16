### FastAPI backend
###### Websocket with API


```zsh
# Install
python3 -m venv venv
# comment
source venv/bin/activate
# comment
pip install -r requirements.txt
```

```zsh
# run
fastapi dev main.py
# or for production
uvicorn main:app --host 0.0.0.0 --port 8080 --workers 1
```

```zsh
# deploy
sudo nano /etc/systemd/system/fastapi.service
# cfg
[Unit]
Description=FastAPI application
After=network.target

[Service]
User=user
Group=user
WorkingDirectory=/home/user/fastapi
ExecStart=/home/user/fastapi/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8080 --workers 1
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```