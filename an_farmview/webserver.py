import json
from flask import Flask
from flask import render_template

app = Flask(__name__)
import an_farmview.snmp

@app.route("/")
def temperatures():
    # all the data is made in javascript in the template from api_temp api
    return render_template('temperatures.html')

@app.route('/api/temp')
def api_temp():
    temperature_front = an_farmview.snmp.get_temperature_front()
    temperature_rear = an_farmview.snmp.get_temperature_rear()
    data = {
        'front': temperature_front,
        'rear': temperature_rear,
        }
    
    return json.dumps(data)