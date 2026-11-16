#!/bin/bash
# Double-clic : CINÉLUX V2 avec la barre d'appareils (Pixel, iPhone SE, tablette, bureau…), via serveur local
cd "$(dirname "$0")"
PORT=8731
if ! lsof -ti tcp:$PORT >/dev/null 2>&1; then
  nohup python3 -m http.server $PORT --bind 127.0.0.1 >/dev/null 2>&1 &
  sleep 1
fi
open -a "Google Chrome" "http://localhost:$PORT/index.html#dev"
