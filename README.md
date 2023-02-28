# Tutorial

Following a tutorial to build a simple web app using Django.

# Useful commands

````bash
# create a project called my_project
django-admin startproject my_project
````

````bash
# start the dev server
python3 manage.py runserver
````

````bash
# (re)create the database
python3 manage.py migrate
````

````bash
# create the app my_app in the current project
python3 manage.py startapp my_app
````

````bash
# Start django shell
python3 manage.py shell
````

# Migrations

Migrations are a way to configure the database.

````bash
# Create a migration after model modification
python3 manage.py makemigrations
````

# Apps

Django projects are organized by apps. Each apps has a function and can be activated/deactivated and used in other projects.

Apps have to be added to the end of the **INSTALLED_APPS** list of `project_name/settings.py` to be loaded at the end (after the django's apps).
