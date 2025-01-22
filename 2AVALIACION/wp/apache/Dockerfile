# Usar la imagen base de Debian 12
FROM debian:12

# Actualizar los repositorios, instalar Apache y PHP
RUN apt update && \
    apt install -y apache2 php libapache2-mod-php php-mysqli -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    a2enmod ssl && \
    a2enmod rewrite

# Exponer los puertos 80 y 443 para Apache
EXPOSE 80 443

# Iniciar Apache en primer plano
CMD ["apachectl", "-D", "FOREGROUND"]
