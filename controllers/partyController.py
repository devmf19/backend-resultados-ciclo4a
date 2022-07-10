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
        new_student = Party(info)
        return self.repository.save(new_student)

    def show(self, id):
        print("Obteniendo un parrtido por id: ", id)
        return self.repository.findById(id)

    def update(self, id, info):
        print("Actualizando un partido por id: ", id)
        old_party = Party(self.repository.findById(id))
        old_party.name = info["name"]
        old_party.motto = info["motto"]
       
        return self.repository.save(old_party)

    def delete(self, id):
        print("Eliminando un partido por id: ", id)
        return self.repository.delete(id)
