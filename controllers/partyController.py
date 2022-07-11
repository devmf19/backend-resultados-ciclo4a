from flask import abort
from models.party import Party
from repositories.partyRepository import PartyRepository


class PartyController():
    def __init__(self):
        print("Creando controlador Partidos")
        self.repository = PartyRepository()

    def index(self):
        print("Listar todos los partidos")
        return self.repository.findAll()

    def create(self, info):
        print("Creando un partido")
        new_party = Party(info)
        return self.repository.save(new_party)

    def show(self, id):
        print("Obteniendo un parrtido por id: ", id)
        party_found = self.repository.findById(id)
        if(party_found):
            return party_found
        abort(404, description="Party not found")    
        

    def update(self, id, info):
        print("Actualizando un partido por id: ", id)
        old_party = Party(self.repository.findById(id))
        old_party.name = info["name"]
        old_party.motto = info["motto"]
       
        return self.repository.save(old_party)

    def delete(self, id):
        print("Eliminando un partido por id: ", id)
        return self.repository.delete(id)
    
