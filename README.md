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

~~~run the flask app (with `--debug` for dev)~~~
```bash
poetry run python -m flask --app an_farmview.webserver.py run --host=0.0.0.0
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
when copying DATABASE_URL from heroku into `.env`
poetry needs `postgresql://` instead of `postgres://`

sqlalchemy needs `psycopg2` for some reason not installed with it.
```bash
poetry add psycopg2
```