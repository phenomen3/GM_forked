# Gestión y Monitoreo

Sistema creado para el area de monitoreo inteligente del C5.

- Este proyecto fue desarrollado en un ambiente coon SO **Ubuntu 20.04 LTS**

## Configuración

Para correr y poder colaborar con este proyecto es necesario tener instalado las siguientes herramientas en tu maquina.

1. Python
2. Django
3. Python Virtual environment
4. SGBD (PostgreSQL)

### Instalación de SW

Instala pytho, pip y postgreSQL

> apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib curl

Instala el ambiente virutal de Python

> -H pip3 install virtualenv

Crea un ambiente virtual en el directorio de tu proyecto

> virtualenv server_env

Habilita tu ambiente virtual

> source server_env/bin/activate

una vez dentro hay que instalar Django

> pip install django

### Repositorio git

Ingresa al siguiente [**ENLACE**](https://github.com/micaila/GM) y Clona o descarga el repositorio.

## Migraciones

Al mismo nivel que tu archivo *manage.py* corremos los siguientes comandos para migrar correctamente los modelos.

> manage.py makemigrations

>manage.py migrate

# Prueba el sitio

Para testear el sitio prueba el siguiente comando:

> manage.py runserver



