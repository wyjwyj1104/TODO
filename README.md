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

2. Run server locally

   ```sh
   ./manage.py makemigrations
   ./manage.py migrate
   ./manage.py runserver
   ```

3. How to test
  ```sh
  Go to web browser "http://127.0.0.1:8000/"
  Click "login" to log in
  Type in username and password ("user01", "superdupersecure01")
  Click "logout" to log out
  Click "TODO List" to view TODO list
  Click "create" to create TODO with inputs
  Click "update" to update a TODO with new inputs
  Click "delete", Click "Yes, delete" to confirm deleting a TODO from list
  ```

### Recommended users for testing
| Username | Password |
| --- | --- |
| user01 | superdupersecure01 |
