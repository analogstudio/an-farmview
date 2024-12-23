# an-farmview

Python 3.11.3, FastAPI based webpage using SNMP to get temperatures, all running via [poetry](https://python-poetry.org/).
  - Run `client/record_temp.bat` locally at an interval to record temperatures to the database
  - Web page (`main.py/home.html`) only reads data from the database
  - Web page refreshes every 30 seconds


create `/an_farmview/.env` file to set some environment variables, use `env_template.txt` as an example:
```bash
SNMP_COMMUNITY=public
SNMP_IP=ip of snmp device
```

Make sure poetry is using Python 3.11

```bash
$ where python
C:\Program Files\Python311\python.exe
```

```bash
poetry env use "C:\Program Files\Python311\python.exe"
```

first time install dependencies
```bash
poetry install
```

# Client
### Record temperature from SNMP
Create a scheduled task to run the client bat file `an_farmview/client/record_temp.bat` at a 5min interval or whatever you like.

# Dev

run fastapi via uvicorn, use same port as flask did and allow other IPs
```bash
poetry run uvicorn an_farmview.main:app --reload --host 0.0.0.0 --port 5000
```
Uses jinja2 templates just like flask but need to [install manually](https://fastapi.tiangolo.com/advanced/templates/) 

runs here
```bash
http://localhost:5000/
```

### UBL
This script lists the features hosted on your license server. You'll need to set up a password first:
 
1. Login to end user portal (thinkbox.flexnetoperations.com)
2. Click Search Servers from the option on the right
3. Click the License Server ID (note the ID for later)
4. On the View Server page click the Set Password option (far right of the options displayed above Add-Ons)

The Set Password page lists some password rules and allows the user to set the password for the ‘admin’ user
 
Once that is set, you'll need to set two environment variables:

FNO_SERVER: The server ID you spotted in step 3 earlier
FNO_PASSWORD: The password you set in step 4

To set these safely on Linux to avoid keeping the password in history
or the environment it's best to run the script like so:

## Heroku
When you manually copy $DATABASE_URL from heroku into `.env` copy it verbatum, it will be converted to `postgresql://` instead of `postgres://` so it works local and on heroku

sqlalchemy needs `psycopg2` for some reason not installed with it.
```bash
poetry add psycopg2
```

## Alembic migrations
Just like in django but needed to set it up [https://devpress.csdn.net/python/62f5096cc6770329307fb178.html](I followed this article)

```bash
poetry add alembic

# init migrations (first time only)
poetry run alembic init migrations

# make migration(revision?)
poetry run alembic revision --autogenerate -m "added vray ubl"

# migrate
poetry run alembic upgrade head
```