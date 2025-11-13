#!/bin/sh
set -e

PUID="${PUID:-1036}"
PGID="${PGID:-100}"

# Check if group exists, create if not
if ! getent group "$PGID" >/dev/null; then
    addgroup -g "$PGID" appgrp
fi
GRP_NAME=$(getent group "$PGID" | cut -d: -f1)

# Check if user exists, create if not
if ! getent passwd "$PUID" >/dev/null; then
    adduser -D -u "$PUID" -G "$GRP_NAME" appuser
fi
USER_NAME=$(getent passwd "$PUID" | cut -d: -f1)

# Ensure nginx directories have correct ownership
chown -R "$USER_NAME":"$GRP_NAME" /var/cache/nginx /var/log/nginx /usr/share/nginx/html 2>/dev/null || true

echo "========================================="
echo "Horoscope Frontend"
echo "========================================="
echo "Configuration:"
echo "  - User: $USER_NAME:$GRP_NAME (UID=$PUID, GID=$PGID)"
echo "  - Port: 8080"
echo "========================================="
echo "Starting Nginx..."
echo "========================================="

# Execute with correct user using su-exec
exec su-exec "$USER_NAME":"$GRP_NAME" "$@"
