from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello Flask! </p>"

db = []

@app.route("/t/<t>")
def getTemp(t):
    return f"Temperature: {escape(t)}!"

@app.route("/h/<h>")
def getHumidity(h):
    return f"Humidity: {escape(h)}!"

@app.route("/th")
def getTemperatureHumidity():
    global db
    args = request.args
    db += [[args.get("t"), args.get("h")]]
    return db

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'