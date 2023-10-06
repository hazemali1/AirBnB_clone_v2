# set up web server

exec { 'set_up':
  command  => 'apt-get update;
  apt-get install -y nginx;
  mkdir -p /data/;
  mkdir -p /data/web_static/;
  mkdir -p /data/web_static/releases/;
  mkdir -p /data/web_static/shared/;
  mkdir -p /data/web_static/releases/test/;
  echo "Hello School" > /data/web_static/releases/test/index.html;
  rm -fr /data/web_static/current;
  ln -s /data/web_static/releases/test/ /data/web_static/current;
  chown -hR ubuntu:ubuntu /data/;
  sed -i "/^server {/a location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell
}
