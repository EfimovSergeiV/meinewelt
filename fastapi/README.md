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

# System.d cfg
[Unit]
Description=FastAPI application
After=network.target

[Service]
User=user
Group=user
WorkingDirectory=/home/user/meinewelt/fastapi
ExecStart=/home/user/meinewelt/fastapi/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8080 --workers 1
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```


```zsh
# Simple NGINX
sudo cat /etc/nginx/sites-enabled/fastapi

# cfg
server {    
    client_max_body_size 3G;
    server_name api.domain.ru;

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8080/;
    }

    location /ws {
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_pass http://127.0.0.1:8080;
    }

}

```


```zsh
# Install
npm install -g wscat

# Connect to websocket
wscat -c ws://api.meinewelt.ru/ws

# for production
wscat -c wss://api.meinewelt.ru/ws
```