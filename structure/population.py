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
        self.getPopulation()[index] = score
    def addElementPopu(self,e):
        self.getPopulation().append(e)


    def resetPopulation(self):
        self.setPopulation([])

    def genInstruction(self,txt):
        a = Instruction()
        a.generateCode(txt)
        return a
    def getInstructionSkeleton(self):
        i = []
        i.append(self.genInstruction("PUSH 1 5"))
        i.append(self.genInstruction("PUSH 2 5"))
        i.append(self.genInstruction("PUSH 3 5"))
        result = Algorithm(instructions=i)
        return result
    def createPopulation(self,config):
        self.resetPopulation()
        #create random algorithm
        algorithmSkeleton = self.getInstructionSkeleton()

        for i in range((config.getPopulation())):
            self.getPopulation().append(elementPopulation(algorithmSkeleton))
    def getElements(self):
        return self.getPopulation()
    def showAll(self):
        for i in self.getPopulation():
            i.showElement()
    def countPopulation(self):
        return len(self.population)

