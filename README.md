# an-farmview

Python 3.8, Flask based webpage using SNMP to get temperatures, all running via poetry.
Refreshes every 30seconds

create `/an_farmview/.env` file to set some environment variables, use `env_template.txt` as an example:
```bash
SNMP_COMMUNITY=public
SNMP_IP=ip of snmp device
```

run it (with `--debug` for dev)
```bash
poetry run python -m flask --app an_farmview.webserver.py run --host=0.0.0.0
```

