from functools import reduce
from repositories.interfaceRepository import InterfaceRepositorio
from models.pollingStation import PollingStation
from flask import jsonify

class PollingStationRepository(InterfaceRepositorio[PollingStation]):
    def countAllvotes(self, id):
        laColeccion = self.baseDatos[self.coleccion]
        pipeline = [
            {"$unwind":"$candidatos"},
            {"$match":{}},
            {"$group":{ 
                "_id":"$candidatos._id",
                "votos":{"$sum":"$candidatos.candidato.votos"}
                }}
        ]
        result = list(laColeccion.aggregate(pipeline))
        total = sum(x["votos"] for x in result)

        return jsonify(total)
    
    def countCandidateVotes(self):
        laColeccion = self.baseDatos[self.coleccion]
        pipeline = [
            {"$unwind":"$candidatos"},
            {"$match":{}},
            {"$group":{ 
                "_id":"$candidatos._id",
                "votos_candidato":{"$sum":"$candidatos.votos"},
                "canditato_name":{"$first":"$candidatos.name"},
                "canditato_lastname":{"$first":"$candidatos.last_name"},
                }}
        ]
        result = list(laColeccion.aggregate(pipeline))
        return jsonify(result)
    
    def countPartyVotes(self):
        laColeccion = self.baseDatos[self.coleccion]
        party_search = [
            {"$unwind":"$candidatos"},
            {"$match":{}},
            {"$group":{ 
                "_id":"$candidatos.partido",
                "votos":{"$sum":"$candidatos.votos"},
                }}
        ]
        
        candidates_search = [
            {"$unwind":"$candidatos"},
            {"$match":{}},
            {"$group":{
                "_id": "$candidatos._id",
                "votos_candidato":{"$sum":"$candidatos.votos"},
                "canditato_name":{"$first":"$candidatos.name"},
                "canditato_lastname":{"$first":"$candidatos.last_name"},
                "party":{"$first":"$candidatos.partido"}
            }}
        ]
        
        party_votes = list(laColeccion.aggregate(party_search))
        candidate_votes = list(laColeccion.aggregate(candidates_search))
        
        result = []
        for party in party_votes:        
            party_candidates = []
            for candidate in candidate_votes:
                if party["_id"] == candidate["party"]:
                    party_candidates.append(candidate)     
            party["candidatos"] = party_candidates
            result.append(party)
                    
        return jsonify(result)
