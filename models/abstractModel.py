from abc import ABCMeta #simulation abstact class in python

class AbstractModel(metaclass=ABCMeta):
    def __init__ (self, data):
        for k, v in data.items(): #running a dictionary DATA
            setattr(self, k, v) #Make atributes in the class, with KEYS as names of atibutes and values as values of atributes