from flask import Response, abort
from models.candidato import Candidato
from models.party import Party
from repositories.candidateRepository import CandidateRepository
from repositories.partyRepository import PartyRepository


class CandidateController():

    def __init__(self):
        print("Creando controlador Candidato")
        self.repository = CandidateRepository()
        self.partyRepository = PartyRepository()

    def index(self):
        print("Listar todas los candidatos")
        return self.repository.findAll()

    def create(self, info):
        print("Creando un candidato")
        party_id = info['partido_id']
        info.pop("partido_id")
        party = Party(self.partyRepository.findById(party_id))
        new_candidate = Candidato(info)
        new_candidate.partido = party
        return self.repository.save(new_candidate)

    def show(self, id):
        print("Obteniendo un candidato por id: ", id)
        candidate_found = self.repository.findById(id)
        if (candidate_found):
            return candidate_found
        abort(404, description="Candidate not found")

    def update(self, id, info):
        print("Actualizando un candidato por id: ", id)
        old_candidate = Candidato(self.repository.findById(id))
        old_candidate.last_name = info["last_name"]
        old_candidate.name = info["name"]
        partido_id = info["partido"]
        party = Party(self.partyRepository.findById(partido_id))
        old_candidate.partido = party

        return self.repository.save(old_candidate)

    def delete(self, id):
        print("Eliminando una candidato por id: ", id)
        return self.repository.delete(id)
