from flask import Flask, send_from_directory
from threading import Thread
import json


app = Flask('')
app.config['UPLOAD_FOLDER'] = "files/video/"


@app.route("/")
def index():
    return "Nothing To see here"


@app.route("/backup/<id>")
@app.route("/backup/<id>.json")
def getrules(id):
    try:
        with open(f"data/backups/{id}.json") as f:
            return "<pre>"+f.read()+"</pre>"
    except FileNotFoundError:
        return "<pre>User has no backups</pre>"
    else:
        return "<pre>Unknown error</pre>"

@app.route('/<file>')
def returnfile(file):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], file)
    except:
        return f"File '{file}' not found"


def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
