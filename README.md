# an-farmview

Python 3.8, Flask based webpage using SNMP to get temperatures, all running via [poetry](https://python-poetry.org/).
Refreshes every 30seconds


create `/an_farmview/.env` file to set some environment variables, use `env_template.txt` as an example:
```bash
SNMP_COMMUNITY=public
SNMP_IP=ip of snmp device
```

Make sure poetry is using Python 3.8

```bash
$ where python
C:\Program Files\Python38\python.exe
C:\Python37\python.exe
C:\Python27\python.exe
C:\Users\sreeves\AppData\Local\Microsoft\WindowsApps\python.exe
C:\Users\sreeves\AppData\Roaming\pypoetry\venv\Scripts\python.exe
```

```bash
poetry env use "C:\Program Files\Python38\python.exe"
```

first time install dependencies
```bash
poetry install
```

run the flask app (with `--debug` for dev)
```bash
poetry run python -m flask --app an_farmview.webserver.py run --host=0.0.0.0
```

runs here
```bash
http://localhost:5000/
```
