# issy_web_project
Crear el folder y guardar el proyecto

mkdir issy_web_project && cd issy_web_project

Crear y activar el entorno virtual

virtualenv issy_web_project_env && cd issy_web_project_env

Para linux:

source bin/activate

Para windows:

scripts/activate

Clonar el Proyecto:

git clone https://github.com/andialuis/issy_web_project.git

Instalar Requerimientos

pip install -r requirements.txt

o

pip3 install -r requirements.txt


Correr las migraciones de bases de datos

python manage.py migrate

Crear un superusuario

pythono manage.py createsuperuser

Llenar solo usuario y contraseña (email no es necesario)

Correr el proyecto:

python manage.py runserver
