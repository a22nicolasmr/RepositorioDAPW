FROM debian:12

RUN apt update && apt install -y apache2

RUN a2enmod ssl

EXPOSE 80
EXPOSE 443

CMD ["apache2ctl", "-D", "FOREGROUND"]