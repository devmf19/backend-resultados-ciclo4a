from tokenize import group
from flask import abort
from models.pollingStation import PollingStation
from models.candidato import Candidato

from repositories.pollingStationRepository import PollingStationRepository
from repositories.candidateRepository import CandidateRepository

from flask import jsonify


class PollingStationController():
    def __init__(self):
        print("Creando controlador Mesa")
        self.repository = PollingStationRepository()
        self.candidateRepository = CandidateRepository()

    def index(self):
        print("Listar todas las mesas")
        return self.repository.findAll()

    def create(self, info):
        print("Creando mesa")
        result =self.repository.createPollingStation(info)

       # new_ps = PollingStation(result)
       # print(new_ps)
       # result = self.repository.save(new_ps)
        return result

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
        for temp in result:
            acceptedCandidateId = temp['_id']
            try:
                candidate = self.candidateRepository.findById(acceptedCandidateId)
            except:
                print("Advertencia, no se encuentra información completa del candidato:" + acceptedCandidateId)
                continue
            temp['name'] = candidate['name']
            temp['last_name'] = candidate['last_name']
        return (result)

    def getCandidateVotesById(self, id):
        result = self.repository.countCandidateVotesById(id)
        for temp in result:
            acceptedCandidateId = temp['_id']
            try:
                candidate = self.candidateRepository.findById(acceptedCandidateId)
            except:
                print("Advertencia, no se encuentra información completa del candidato:" + acceptedCandidateId)
                continue
            temp['name'] = candidate['name']
            temp['last_name'] = candidate['last_name']
        return (result)


    def getAllVotes(self):
        result = self.repository.countAllvotes()
        return jsonify(result)

    def getNewSenate(self):
        candidatesVotes = self.repository.countAllvotes()
        sortedList = sorted(candidatesVotes, key=lambda x: x['votos'], reverse=True)
        acceptedCandidates=sortedList[0:15]
        uniqueParties=set()
        resultDict={}
        for temp in acceptedCandidates:
            #find party of candidate
            acceptedCandidateId=temp['_id']
            try:
                candidate=self.candidateRepository.findById(acceptedCandidateId)
            except:
                print("Advertencia, no se encuentra información completa del candidato:" +acceptedCandidateId)
                continue
            partyName= candidate['partido']['name']
            if partyName in resultDict:
                count=resultDict[partyName]
                count=count+(100/15)
                resultDict[partyName]=count
            else:
                resultDict[partyName]=(100/15)
        #print(resultDict)

        return resultDict

    def getPartyVotes(self):
        candidatesVotes = self.repository.countAllvotes()

        uniqueParties=set()
        resultDict={}
        for temp in candidatesVotes:
            #find party of candidate
            acceptedCandidateId=temp['_id']
            try:
                candidate=self.candidateRepository.findById(acceptedCandidateId)
            except:
                print("Advertencia, no se encuentra información completa del candidato:" +acceptedCandidateId)
                continue
            partyName= candidate['partido']['name']
            if partyName in resultDict:
                count=resultDict[partyName]
                count=count+temp["votos"]
                resultDict[partyName]=count
            else:
                resultDict[partyName]=temp["votos"]
        #print(resultDict)

        return resultDict


    def getPartyVotesbyID(self, id):
        candidatesVotes = self.repository.countAllvotes()

        uniqueParties=set()
        resultDict={}
        for temp in candidatesVotes:
            #find party of candidate
            acceptedCandidateId=temp['_id']
            try:
                candidate=self.candidateRepository.findById(acceptedCandidateId)
            except:
                print("Advertencia, no se encuentra información completa del candidato:" +acceptedCandidateId)
                continue
            partyName= candidate['partido']['name']
            if candidate['partido']['_id']!=id:
                continue

            if partyName in resultDict:
                count=resultDict[partyName]
                count=count+temp["votos"]
                resultDict[partyName]=count
            else:
                resultDict[partyName]=temp["votos"]
        #print(resultDict)

        return resultDict
