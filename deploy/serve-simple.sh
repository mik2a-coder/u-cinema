#!/usr/bin/env bash
# Test rapide SANS nginx (Mac ou Raspberry) : sert le dossier sur le port 8080.
cd "$(dirname "$0")/.."
echo "U CINEMÀ sur http://$(hostname -I 2>/dev/null | awk '{print $1}' || ipconfig getifaddr en0):8080"
exec python3 -m http.server 8080 --bind 0.0.0.0
