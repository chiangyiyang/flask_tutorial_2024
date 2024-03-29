from flask import Flask, request

app = Flask(__name__)
db = []

@app.route("/th")
def getTemperatureHumidity():
    global db
    args = request.args
    if args.get("t") is not None and args.get("h") is not None:
        db += [[args.get("t"), args.get("h")]]

    return db


if __name__ == '__main__':
    app.run(port=3000, debug=True)
