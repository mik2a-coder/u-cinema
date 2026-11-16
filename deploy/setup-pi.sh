#!/usr/bin/env bash
# À exécuter SUR le Raspberry (en root) : publie U CINEMÀ (nginx + pare-feu local + Tailscale Serve).
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"
WEB=/var/www/cinelux
PORT="${PORT:-8080}"          # port local (nginx)
TS_PORT="${TS_PORT:-8443}"    # port HTTPS Tailscale (distinct pour ne rien écraser)

if ! command -v nginx >/dev/null 2>&1; then apt-get update && apt-get install -y nginx; fi

mkdir -p "$WEB"
rm -rf "${WEB:?}"/*
cp -r "$SRC/index.html" "$SRC/manifest.webmanifest" "$SRC/sw.js" "$SRC/fonts" "$SRC/icons" "$SRC/img" "$WEB"/
chown -R www-data:www-data "$WEB"

mkdir -p /etc/nginx/snippets
cp "$SRC/security-headers.conf" /etc/nginx/snippets/cinelux-security.conf
sed "s/__PORT__/$PORT/g" "$SRC/nginx-cinelux.conf" > /etc/nginx/conf.d/cinelux.conf
nginx -t
systemctl enable nginx >/dev/null 2>&1 || true
systemctl reload nginx 2>/dev/null || systemctl restart nginx

# Pare-feu : si ufw est actif, autoriser le port UNIQUEMENT depuis le réseau local (pas depuis Internet)
if command -v ufw >/dev/null 2>&1 && ufw status | grep -q "Status: active"; then
  ufw allow from 192.168.0.0/16 to any port "$PORT" proto tcp >/dev/null && echo "Pare-feu : port $PORT ouvert pour le réseau local."
fi

# Tailscale : accès HTTPS privé (valide pour installer l'appli). On ne touche à rien d'existant.
if command -v tailscale >/dev/null 2>&1; then
  if tailscale serve status 2>/dev/null | grep -q ":$TS_PORT"; then
    echo "Tailscale : le port $TS_PORT est déjà utilisé, je ne change rien (relancez avec TS_PORT=8444)."
  else
    tailscale serve --bg --https="$TS_PORT" "http://localhost:$PORT" 2>/dev/null \
      || tailscale serve --bg --https="$TS_PORT" "localhost:$PORT" \
      || echo "Tailscale : configuration automatique impossible (voir LISEZ-MOI.md)."
  fi
  echo; echo "--- Tailscale Serve :"; tailscale serve status || true
fi

IP="$(hostname -I | awk '{print $1}')"
echo
echo "U CINEMÀ est en ligne :"
echo "  Réseau local : http://$IP:$PORT"
echo "  À distance   : voir l'adresse https://…ts.net:$TS_PORT ci-dessus"
