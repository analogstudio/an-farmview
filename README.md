# an-farmview

Python 3.11.3, ~~Flask~~ FastAPI based webpage using SNMP to get temperatures, all running via [poetry](https://python-poetry.org/).
Refreshes every 30seconds


create `/an_farmview/.env` file to set some environment variables, use `env_template.txt` as an example:
```bash
SNMP_COMMUNITY=public
SNMP_IP=ip of snmp device
```

Make sure poetry is using Python 3.11.3

```bash
$ where python
...
C:\Program Files\Python311\python.exe
...
```

```bash
poetry env use "C:\Program Files\Python311\python.exe"
```

first time install dependencies
```bash
poetry install
```


run fastapi via uvicorn, use same port as flask did and allow other IPs
```bash
poetry run uvicorn an_farmview.main:app --reload --host 0.0.0.0 --port 5000
```
Uses jinja2 templates just like flask but need to [install manually](https://fastapi.tiangolo.com/advanced/templates/) 

runs here
```bash
http://localhost:5000/
```

## heroku
When copying DATABASE_URL from heroku into `.env` copy it verbatum, it will be converted to `postgresql://` instead of `postgres://` so it works local and on heroku

sqlalchemy needs `psycopg2` for some reason not installed with it.
```bash
poetry add psycopg2
```

## Alembic migrations
Just like in django but needed to set it up [https://devpress.csdn.net/python/62f5096cc6770329307fb178.html](I followed this article)
```bash
poetry add alembic

# make migrations
poetry run alembic init migrations

# migrate
poetry run alembic upgrade head
```