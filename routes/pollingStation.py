from main import app
from flask import jsonify, request, Response
import json

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
    return response

@app.route("/table/<string:id>", methods=["PUT"])
def update_ps(id):
    info = request.get_json(force=True)
    response = ps_controller.update(id, info)
    return jsonify(response)

@app.route("/table/<string:id>", methods=["DELETE"])
def delete_ps(id):
    response = ps_controller.delete(id)
    return jsonify(response)


@app.route("/newsenate", methods=['GET'])
def get_newSenate():
    response = ps_controller.getNewSenate()
    print(response)
    return jsonify(response)


@app.route("/candidates-result", methods=['GET'])
def getAllCandidatesResults():
    response = ps_controller.getCandidateVotes()
    return jsonify(response)

@app.route("/candidates-result/<string:id>", methods=['GET'])
def getCandidateResultsByID(id):
    response = ps_controller.getCandidateVotesById(id)
    return jsonify(response)

@app.route("/parties-result/", methods=['GET'])
def getPartiesResult():
    response = ps_controller.getPartyVotes()
    return Response(json.dumps(response), mimetype='application/json')

@app.route("/parties-result/<string:id>", methods=['GET'])
def getPartiesResultbyId(id):
    response = ps_controller.getPartyVotesbyID(id)
    return jsonify(response)
