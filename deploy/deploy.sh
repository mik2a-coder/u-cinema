#!/usr/bin/env bash
# À exécuter SUR LE MAC : envoie U CINEMÀ au Raspberry et le publie.
# Usage : ./deploy/deploy.sh pi@raspberrypi.local      (ou pi@192.168.1.xx)
set -euo pipefail
HOST="${1:?Usage: ./deploy/deploy.sh utilisateur@adresse-du-raspberry}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

cp -r "$HERE/index.html" "$HERE/manifest.webmanifest" "$HERE/sw.js" "$HERE/fonts" "$HERE/icons" "$HERE/img" "$STAGE"/
cp "$HERE/deploy/setup-pi.sh" "$HERE/deploy/nginx-cinelux.conf" "$HERE/deploy/security-headers.conf" "$STAGE"/

rsync -az --delete "$STAGE"/ "$HOST":/tmp/cinelux-site/
ssh -t "$HOST" "sudo PORT=${PORT:-8080} bash /tmp/cinelux-site/setup-pi.sh"
