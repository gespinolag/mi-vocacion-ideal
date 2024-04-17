# APP "MI VOCACIÓN IDEAL"
Este proyecto consiste en el desarrollo de un prototipo de orientación vocacional gamificado en el marco de la realización de un proyecto final de grado para la obtención del título de Ingeniería Informática.

El presente proyecto fue desarrollado en el lenguaje de programación Python y el framework de desarrollo web Django.

## Procedimiento de instalación y montaje del proyecto en un ambiente local
### Python
**Linux:**
- Verificar antes si cuentas con una versión instalada de Python con el comando `python --version`
- Abrir una terminal y ejecutar el comando `sudo apt update`
- Instalar Python en su versión `3.x.x` con el comando `sudo apt install python3`
- Una vez culminada la instalación puedes verificar nuevamente la versión instalada desde una terminal con el comando `python --version`

**Windows:**
- Descarga el instalador de Python desde el sitio [web oficial](https://www.python.org/downloads/windows/ "web oficial")
- En la instalación, agregar Python a tu variable PATH del sistema. Para más información visitar este [enlace](https://docs.python.org/es/3.11/using/windows.html "enlace").

### MySQL
**Linux:**
Se requiere instalar el motor de base datos MySQL. Para ello puedes seguir el siguiente enlace donde se explica detalladamente la instalación para sistemas operativos Linux: [How To Install MySQL on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-22-04 "How To Install MySQL on Ubuntu 22.04")

**Windows:**
Se requiere instalar el motor de base datos MySQL. Para ello puedes seguir el siguiente enlace donde se explica detalladamente la instalación para sistemas operativos Windows: [MySQL Installer](https://dev.mysql.com/downloads/installer/ "MySQL Installer")

### Pip
**Linux:**
Es necesario tener instalado el gestor de paquetes Pip. Para instalarlo en Linux ejecute en una terminal el comando: `sudo apt update` y por último el comando `sudo apt install python3-pip`

**Windows:**
Es necesario tener instalado el gestor de paquetes Pip. Para instalarlo en Windows ejecute en un CMD el comando: `python -m pip install --upgrade pip`, luego puede verificar la versión instalada con el  comando `pip --version`

### Entorno virtual (venv)
**Linux:**
- Instala virtualenv si no lo tienes, ejecutando en una terminal el comando: `sudo pip install virtualenv`
- Navega hasta el directorio del proyecto con una terminal y crea el entorno virtual ejecutando el comando: `python3 -m venv nombre_del_entorno` reemplazando el nombre por uno de su preferencia, por ejemplo **venv**
- Una vez creado el entorno virtual, puedes activarlo desde el directorio del proyecto con el comando `source nombre_del_entorno/bin/activate` 

**Windows**
- Instala virtualenv si no lo tienes, ejecutando en un CMD el comando: `pip install virtualenv`
- Navega hasta el directorio del proyecto con el CMD y crea el entorno virtual ejecutando el comando: `python -m venv nombre_del_entorno` reemplazando el nombre por uno de su preferencia, por ejemplo **venv**
- Una vez creado el entorno virtual, puedes activarlo con el CMD desde el directorio del proyecto con el comando `nombre_del_entorno\Scripts\activate` 

### Instalación de dependencias del proyecto
- Abrir una terminal Linux o ventana CMD Windows
- Navega hasta el directorio del proyecto utilizando el comando `cd`
- Ejecuta el siguiente comando para iniciar la instalación de las dependencias del proyecto: `pip install -r requirements.txt`
- Verifica que se hayan instalado las dependencias correctamente con el comando: `pip list`

### Configuración de la Base de Datos en el proyecto
En el archivo settings.py del proyecto, identifica las siguientes líneas de código para configurar la Base de Datos
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'databaseName',
        'USER': 'myUser',
        'PASSWORD': 'myPassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
donde ` 'NAME': 'mivocacionideal'` es el nombre de la base de datos. Puedes crear la misma accediendo con el comando `mysql -u miUsuario -p` y luego ejecutando el comando `CREATE DATABASE mivocacionideal;`, luego `'USER': 'myUser'`y ` 'PASSWORD': 'myPassword'` representan el nombre de usuario y contraseña creados previamente cuando instaló el motor de base de datos. Los demás parámentros se pueden dejar así como están por defecto si ejecutará de forma local el proyecto.

### Ejecución del proyecto
Puedes utilizar un editor de código como Visual Studio Code o bien el IDE PyCharm para proyectos Python.

**Linux**
Teniendo el entorno virtual previamente activado, ejecuta desde un terminal los siguientes comandos:
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`
- `python3 manage.py runserver`

**Windows**
Teniendo el entorno virtual previamente activado, ejecuta desde un terminal los siguientes comandos:
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`

Una vez que el servidor se haya iniciado, puedes abrir en tu navegador la url http://127.0.0.1:8000/
