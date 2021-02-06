## Admin tables
    - python manage.py makemigration
    - python manage.py migrate
## Admin page
    - have to create superuser
    - python manage.py createsuperuser
## Crud operations
  - create  new app(python manage.py startapp appname)
  - open settings.py file and Add appname in installed apps
  - open urls.py(project folder)
   - add include
   - create file in app2 rename as 'urls.py'
## table creation syntax
   - class classname(models.model):