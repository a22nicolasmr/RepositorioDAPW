FROM debian:12

RUN apt update && apt install -y apache2 php

RUN sed -i 's/^ServerTokens.*/ServerTokens Prod/g' /etc/apache2/conf-available/security.conf
RUN sed -1 's/^ServerSignature.*/ServerTokens Off/g' /etc/apache2/conf-available/security.conf

EXPOSE 80
EXPOSE 443

CMD ["apachectl", "-D", "FOREGROUND"]