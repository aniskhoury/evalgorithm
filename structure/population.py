from config.evaconfig import *
from structure.instruction import  *
from structure.algorithm import *
from structure.elementPopulation import *
class Population:
    population = []

    def __init__(self,population=[]):
        self.setElements(population)

    def getPopulation(self):
        return self.population
    def setPopulation(self,s):
        self.population = s
    def setElements(self,s):
        self.population = s
    def getElements(self):
        return self.population
    def putScore(self,index,score):
        self.getPopulation()[index]
    def createPopulation(self,config):
        self.setPopulation([])
        for i in range(config.getPopulation()):
            self.population.append(elementPopulation(Algorithm()))
    def showPopulation(self):
        for i in self.getPopulation():
            i.showElement()
    def countPopulation(self):
        return len(self.population)

