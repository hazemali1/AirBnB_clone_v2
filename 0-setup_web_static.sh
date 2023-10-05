#!/usr/bin/env bash
# sets up wep server
apt-get update
apt-get install -y nginx
if ! test -f /data/; then
	mkdir /data/
fi
if ! test -f /data/web_static/; then
	mkdir /data/web_static/
fi
if ! test -f /data/web_static/releases/; then
	mkdir /data/web_static/releases/
fi
if ! test -f /data/web_static/shared/; then
	mkdir /data/web_static/shared/
fi
if ! test -f /data/web_static/releases/test/; then
	mkdir /data/web_static/releases/test/
fi
echo -e '<html>\n <head>\n </head>\n <body>\n  Hello School\n </body>\n</html>' > /data/web_static/releases/test/index.html
if test -f /data/web_static/current; then
	rm -r /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/server {/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart
