FROM debian:12

RUN apt update &&  apt install -y apache2 php

CMD ["apachectl","-D","FOREGROUND"]