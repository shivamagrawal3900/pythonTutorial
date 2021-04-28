To create a Django project from scratch, run following command in in terminal where you want to create the project

`django-admin startproject <projectName>`

To create a new app within the project. Go to project director and run command:

` python3 manage.py startapp <appName>`

To create migrations(Used to store model to DB). This will just create a file to migrate, won't actually migrate.

`python3 manage.py makemigrations`

To migrate

`python3 manage.py migrate`

To access admin panel, a super user will be needed to be created

`python3 manage.py createsuperuser`

To access python shell

`python3 manage.py shell`

