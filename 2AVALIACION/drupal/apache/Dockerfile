FROM debian:12

RUN apt update -y \
    && apt upgrade -y \
    && apt -y install wget curl sudo lsb-release apt-transport-https ca-certificates \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list

RUN apt update && apt install -y apache2 php8.3 \
    php8.3-mysql \
    php8.3-xml \
    php8.3-gd \
    php8.3-curl \
    php8.3-mbstring \
    git \
    zip \
    libnss3-tools \
    xdg-utils \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('sha384', 'composer-setup.php') === 'dac665fdc30fdd8ec78b38b9800061b4150413ff2e3b6f88543c636f7cd84f6db9189d43a81e5503cda447da73c7e5b6') { echo 'Installer verified'.PHP_EOL; } else { echo 'Installer corrupt'.PHP_EOL; unlink('composer-setup.php'); exit(1); }"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"
RUN mv composer.phar /usr/local/bin/composer

RUN a2enmod ssl
RUN a2enmod rewrite

EXPOSE 80
EXPOSE 443

CMD ["apachectl", "-D", "FOREGROUND"]