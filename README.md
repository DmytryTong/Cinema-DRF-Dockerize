# CINEMA API

API-service for cinema-theater, featuring DRF and postgresql database

## Installing using GitHub:

```shell
  git clone https://github.com/DmytryTong/Cinema-DRF-Dockerize.git
  cd Cinema-DRF-Dockerize
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  export POSTGRES_DB=<your own db name>
  export POSTGRES_USER=<your own db username>
  export POSTGRES_PASSWORD=<your own db password>
  export POSTGRES_HOST=<your own db hostname>
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```

## Run with docker:
```shell
  docker-compose build
  docker-compose up
```
  

## Features:

- JWT authenticated
- Admin panel /admin/
- Documentation is located at /api/doc/swagger/
- Managing orders and tickets
- Creating cinema halls
- Creating movies with genres, actors
- Adding movie sessions
- Filtering movies and movie sessions

## Access:
- creating user using /api/user/register/
- managing token using /api/user/token/
