FROM debian:12

RUN apt update && \
    apt install -y apache2 php php-mysql && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN a2enmod ssl
RUN a2enmod rewrite

CMD ["apachectl", "-D", "FOREGROUND"]