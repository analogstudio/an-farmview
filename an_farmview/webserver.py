import json
from flask import Flask
from flask import render_template

app = Flask(__name__)
import an_farmview.snmp
import an_farmview.ubl

@app.route("/")
def home():
    # all the data is made in javascript in the template from api_temp api
    return render_template('home.html')

@app.route('/api/temp')
def api_temp():
    temperature_front = an_farmview.snmp.get_temperature_front()
    temperature_rear = an_farmview.snmp.get_temperature_rear()
    data = {
        'front': temperature_front,
        'rear': temperature_rear,
        }
    
    return json.dumps(data)

@app.route('/api/ubl')
def api_ubl():
    redshift_available = an_farmview.ubl.get_redshift()
    data = {
        'redshift_available': redshift_available,
        }
    
    return json.dumps(data)