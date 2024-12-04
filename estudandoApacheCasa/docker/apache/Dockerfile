FROM debian:12

RUN apt update && apt install -y apache2 php

RUN sed -i 's/^ServerTokens.*/ServerTokens Prod/' /etc/apache2/conf-available/security.conf

RUN sed -i 's/^ServerSignature.*/ServerSignature Off/' /etc/apache2/conf-available/security.conf

EXPOSE 80
EXPOSE 443

CMD ["apachectl", "-D", "FOREGROUND"]
