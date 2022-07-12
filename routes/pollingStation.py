from main import app
from flask import jsonify, request

from controllers.pollingStationController import PollingStationController 

ps_controller = PollingStationController()

@app.route("/tables", methods=['GET'])
def get_pollingStations():
    response = ps_controller.index()
    return jsonify(response)

@app.route("/table/<string:id>", methods=['GET'])
def get_ps(id):
    response = ps_controller.show(id)
    return jsonify(response)    

@app.route("/table", methods=["POST"])
def create_ps():
    info = request.get_json(force=True)
    response = ps_controller.create(info)
    return jsonify(response)   

@app.route("/table/<string:id>", methods=["PUT"])
def update_ps(id):
    info = request.get_json(force=True)
    response = ps_controller.update(id, info)
    return jsonify(response)

@app.route("/table/<string:id>", methods=["DELETE"])
def delete_ps(id):
    response = ps_controller.delete(id)
    return jsonify(response)  