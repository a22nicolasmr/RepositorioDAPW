FROM debian:12


#Instalar paquetes necesarios (apache php extensions php)
RUN apt update && apt install -y php-fpm libapache2-mod-php\
    curl \
    wget \
    git \
    zip \
    php-json \
    php-xml \
    php-gd \
    php-mysql \
    php-pgsql \
    php-zip \
    php-intl \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN a2enmod ssl 
RUN a2enmod rewrite 


EXPOSE 9000

CMD tail -f /dev/null

# CMD ["php8.2-fpm", "-F"]