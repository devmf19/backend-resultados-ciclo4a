from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi

#server initialization
app = Flask(__name__)
cors = CORS(app)


def load_file_config():
    with open("config.json") as configJson:
        data = json.load(configJson)
    return data

#endopints...
@app.route("/", methods=["GET"])
def test():
    response = {
        "message": "Hello world...",
        "errors": []
    }
    return jsonify(response)

# Routes 
import routes.party

#execute server
dataConfig = load_file_config()
url = "http://" + dataConfig['url-backend'] + ":" + str(dataConfig['port'])
print(f"Running server in {url}")
serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])