#!/usr/bin/env bash
# sets up wep server
sudo apt update
sudo apt install -y nginx
mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo -e '<html>\n <head>\n </head>\n <body>\n  Hello School\n </body>\n</html>' > /data/web_static/releases/test/index.html
rm -r /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/server {/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
