from main import app
from flask import jsonify, request

from controllers.candidateController import CandidateController 

candidate_controller = CandidateController()

@app.route("/candidates", methods=['GET'])
def get_candidates():
    response = candidate_controller.index()
    return jsonify(response)

@app.route("/candidate/<string:id>", methods=['GET'])
def get_candidate(id):
    response = candidate_controller.show(id)
    return jsonify(response)    

@app.route("/candidate", methods=["POST"])
def create_candidate():
    info = request.get_json(force=True)
    response = candidate_controller.create(info)
    return jsonify(response)   

@app.route("/candidate/<string:id>", methods=["PUT"])
def update_candidate(id):
    info = request.get_json(force=True)
    response = candidate_controller.update(id, info)
    return jsonify(response)

@app.route("/candidate/<string:id>", methods=["DELETE"])
def delete_candidate(id):
    response = candidate_controller.delete(id)
    return jsonify(response)    