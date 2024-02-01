FROM macbre/nginx-http3
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y
RUN apt-get install -y apt-utils
RUN apt-get install -y curl wget libpq-dev python3-dev gem ruby ruby-dev build-essential libssl-dev libffi-dev python-dev python3-pip zsh
RUN gem install sass
RUN apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev tcl8.6-dev tk8.6-dev python-tk
RUN pip3 install --upgrade pip
RUN apt-get install -y npm
RUN npm install -g less
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN gem install macbre

# pip3 install -r /home/peeljobs/requirements.txt
