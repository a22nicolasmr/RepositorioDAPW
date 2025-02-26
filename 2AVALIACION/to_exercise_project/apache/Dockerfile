FROM debian:12

# Actualizar paquetes e instalar dependencias
RUN apt update && apt upgrade -y \
    && apt install -y wget curl sudo lsb-release git apt-transport-https ca-certificates python3 python3-pip python3-venv \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar Apache y mod_wsgi
RUN apt update && apt install -y apache2 libapache2-mod-wsgi-py3 \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code 

# Crear un entorno virtual y activarlo
RUN python3 -m venv /code/venv
ENV PATH="/code/venv/bin:$PATH"

# Copiar requirements.txt e instalar paquetes dentro del entorno virtual
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r /code/requirements.txt

# Luego copiar el código restante
COPY . /code/

# Habilitar módulos de Apache
RUN a2enmod wsgi ssl

# Configurar Apache para usar el entorno virtual de Python
RUN echo "WSGIPythonHome /code/venv" >> /etc/apache2/apache2.conf

# Comando para mantener Apache en primer plano
CMD ["apache2ctl", "-D", "FOREGROUND"]
