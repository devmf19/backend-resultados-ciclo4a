from repositories.interfaceRepository import InterfaceRepositorio
from models.pollingStation import PollingStation
from models.candidato import Candidato
from repositories.candidateRepository import CandidateRepository
from flask import jsonify

class PollingStationRepository(InterfaceRepositorio[PollingStation]):
    
    # '''================================================================
    # Esta función cuenta todos los votos por cada candidato e todas las mesas'''
    # def countAllvotes(self):
    #     laColeccion = self.baseDatos[self.coleccion]
    #     pipeline = [
    #         {"$unwind":"$candidatos"},
    #         {"$match":{}},
    #         {"$group":{
    #             "_id":"$candidatos._id",
    #             "votos":{"$sum":"$candidatos.candidato.votos"}
    #             }}
    #     ]
    #     result = list(laColeccion.aggregate(pipeline))
    #     total = sum(x["votos"] for x in result)
    #
    #     return total

    '''================================================================
    Esta función cuenta todos los votos por cada candidato e todas las mesas'''
    def countAllvotes(self):
        laColeccion = self.baseDatos[self.coleccion]
        pipeline = [
            {"$unwind":"$candidatos"},
            {"$match":{}},
            {"$group":{
                "_id":"$candidatos.candidato",
                "votos":{"$sum":"$candidatos.votos"}
                }}
        ]
        result = list(laColeccion.aggregate(pipeline))
        return result
    
    '''===============================================================
    Esta funcion crea una lista con cada candidato y sus respectivos resultados'''
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
                "partido":{"$first": "$candidatos.partido"}
                }}
        ]
        result = list(laColeccion.aggregate(pipeline))
        return result
    
    ''' ==============================================================
        La siguiente función obtiene dos listas:
                1) todos los partidos y los votos acumulados para el mismo
                2) todos los candidatos y susresultados electorales 
        de estas listas se crea un diccionario en el que se incluyen
        cada partido con sus resultados acumulados, y dentro del mismo la
        lista con sus candidatos'''
        
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
        ]                                                                   # El formato de salida es
                                                                            # [
        party_votes = list(laColeccion.aggregate(party_search))             #   {
        candidate_votes = list(laColeccion.aggregate(candidates_search))    #       "votos":123,
                                                                            #       "candidatos":[
        result = []                                                         #           {
        for party in party_votes:                                           #               "_id": "62cb489f5158a823ba2172c3",
            party_candidates = []                                           #               "candidato_name":"nombre del candidato",
            for candidate in candidate_votes:                               #               "candidato_lastname":"apellido del candidato",
                if party["_id"] == candidate["party"]:                      #               "party": "partido",
                    party_candidates.append(candidate)                      #               "votos_candidato":123
            party["candidatos"] = party_candidates                          #           },
            result.append(party)                                            #       ]
                                                                            #   },
        return result                                                       # ]

    def createPollingStation(self, info):
        new_ps = PollingStation(info)
        result= self.save(new_ps)
        return jsonify(result)


    # def createPollingStation(self, info):
    #     candidateRepository = CandidateRepository()
    #     candidatos = info['candidatos']
    #     for i in range(len(candidatos)):
    #         candidateid = candidatos[i]['candidate']
    #         found = candidateRepository.findById(candidateid)
    #         if (found):
    #             candidate = Candidato(found)
    #             candidatos[i]['candidate'] = candidate
    #         print(candidatos[i]['candidate'])
    #     new_ps = PollingStation(info)
    #     result= self.save(new_ps)
    #     return jsonify(result)

