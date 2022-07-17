from tokenize import group
from flask import abort
from models.pollingStation import PollingStation
from repositories.pollingStationRepository import PollingStationRepository
from controllers.candidateController import CandidateController
from flask import jsonify


class PollingStationController():
    def __init__(self):
        print("Creando controlador Mesa")
        self.repository = PollingStationRepository()

    def index(self):
        print("Listar todas las mesas")
        return self.repository.findAll()

    def create(self, info):
        print("Creando mesa")
        new_ps = PollingStation(info)
        return self.repository.save(new_ps)

    def show(self, id):
        print("Obteniendo mesa por id: ", id)
        ps_found = self.repository.findById(id)
        if (ps_found):
            return ps_found
        abort(404, description="Polling Station not found")

    def update(self, id, info):
        print("Actualizando mesa por id: ", id)
        old_ps = PollingStation(self.repository.findById(id))
        old_ps.mesa = info["mesa"]
        old_ps.cedulas = info["cedulas"]
        old_ps.candidatos = info["candidatos"]

        return self.repository.save(old_ps)

    def delete(self, id):
        print("Eliminando mesa por id: ", id)
        return self.repository.delete(id)

    def getCandidateVotes(self):
        result = self.repository.countCandidateVotes()
        return jsonify(result)

    def getPartyVotes(self):
        result = self.repository.countPartyVotes()
        return jsonify(result)

    def getAllVotes(self):
        result = self.repository.countAllvotes()
        return jsonify(result)

    def getNewSenate(self):
        candidatesVotes = self.repository.countCandidateVotes()
        sortedList = sorted(candidatesVotes, key=lambda x: x['votos_candidato'], reverse=True)
        return jsonify(sortedList)
