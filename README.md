### Project setup

0. Installation:

   ```sh
   pip3 install django
   pip3 install -r requirements.txt
   ```

1. Create a virtualenv using `pipenv`, install all packages and activate the virtualenv:

   ```sh
   brew install pipenv
   pipenv shell
   ```

2. Run server

   ```sh
   ./manage.py makemigrations
   ./manage.py migrate
   ./manage.py runserver
   ```

### Recommended users for testing
| Username | Password |
| --- | --- |
| user01 | superdupersecure-1 |
