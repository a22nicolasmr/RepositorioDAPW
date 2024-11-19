FROM debian:12

RUN apt update && apt install -y apache2 

EXPOSE 80
EXPOSE 443

CMD ["apachectl", "-D", "FOREGROUND"]