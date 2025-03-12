FROM debian:12


#Instalar paquetes necesarios (apache php extensions php)
RUN apt update && apt install -y apache2 php \
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

#Activar módulos de apache
RUN a2enmod ssl 
RUN a2enmod rewrite 

#Instalar composer

#Instalar ferramentas npm se son necesarias


EXPOSE 80
EXPOSE 443

#Instrución para arrancar apache
CMD ["apache2ctl","-D","FOREGROUND"]