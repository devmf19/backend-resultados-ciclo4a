from main import app
from flask import jsonify, request

from controllers.partyController import PartyController

party_controller = PartyController()

@app.route("/test", methods=["GET"])
def test2():
    info = request.get_json(force=True)
    response = {
        "partido": info["name"],
        "lema": info["motto"]
    }
    
    return jsonify(response)

@app.route("/party", methods=["POST"])
def create_party():
    info = request.get_json(force=True)
    response = party_controller.create(info)
    return jsonify(response)

@app.route("/partys", methods=['GET'])
def get_partys():
    response = party_controller.index();
    return jsonify(response);

@app.route("/party/<string:id>", methods=['GET'])
def get_party(id):
    response = party_controller.show(id);
    return jsonify(response)

@app.route("/party/<string:id>", methods=["PUT"])
def update_party(id):
    info = request.get_json(force=True)
    response = party_controller.update(id, info)
    return jsonify(response)

@app.route("/party/<string:id>", methods=["DELETE"])
def delete_party(id):
    response = party_controller.delete(id)
    return jsonify(response)