#!/usr/bin/env bash
# Sets up a web server for deployment of AirBnB web_static files.

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

cat > /data/web_static/releases/test/index.html <<'EOF'
<html>
  <head>
  </head>
  <body>
    School
  </body>
</html>
EOF

rm -rf /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data/

if ! grep -q "location /hbnb_static/" /etc/nginx/sites-available/default; then
    sed -i '/server_name _;/a\        location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
fi

nginx -t
service nginx restart

exit 0
