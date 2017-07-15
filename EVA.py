from structure.virtualmachine import *
from config.evaconfig import *
from structure.population import *
DEBUG = True
class EVA:
    virtualMachines = []
    config = None
    currentGen = 0
    population = []
    fnFitness = None
    fnCross = None

    def __init__(self,config,virtualMachines=None,fnFitness=None,fnCross=None):
        self.welcomeMessage()
        self.population = Population()
        self.population.createPopulation(config)
        #self.population.showPopulation()
        print("Population num.",self.population.countPopulation())

        if fnFitness == None:
            self.fnFitness = self.funcFitness()
        else:
            self.fnFitness = fnFitness
        if fnCross == None:
            self.fnCross = self.funcCross()
        else:
            self.fnCross = fnCross
    #n -> Number of virtual machines created.
    def funcCross(self):
        return 0
    def funcFitness(self):
        score = 0
        # fer la comprovació desitjada
        return 1 / (1 + (score))
    def createVirtualMachine(self,n=1):
        self.virtualMachines.append(VirtualMachine(memory=512))


    def run(self):
        print("Code run here")
    def showResults(self):
        print("###############################")
        print("########### Results ###########")
        print("###############################")

    def welcomeMessage(self):
        print("################################################")
        print("####### Welcome to Evolutionary Algorithm ######")
        print("#######    Created by Anis Khoury Ribas   ######")
        print("################################################")
