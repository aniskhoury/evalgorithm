from structure.virtualmachine import *
from config.evaconfig import *
from structure.population import *
DEBUG = True
class EVA:
    virtualMachines = []
    config = None
    currentGen = 0
    population = None
    fnFitness = None
    fnCross = None

    def __init__(self,config,virtualMachines=None,fnFitness=None,fnCross=None):
        self.setConfig(config)
        self.createVirtualMachine(n=1)
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
    def setConfig(self,c):
        self.config = c
    #n -> Number of virtual machines created.
    def funcCross(self):
        return 0
    def funcFitness(self):
        score = 0
        # fer la comprovació desitjada
        return 1 / (1 + (score))
    def createVirtualMachine(self,n=1):
        self.virtualMachines.append(VirtualMachine(memory=512))
    def getVirtualMachines(self):
        return self.virtualMachines
    def getPopulation(self):
        return self.population
    def runSimAllAlgorithm(self):
        virMachine = self.getVirtualMachines()[0]
        for element in range(self.getPopulation().countPopulation()):
            #Algorithm was stored in elementPopulation
            algo = self.getPopulation().getElements()[element].getAlgorithm()
            virMachine.loadAlgorithm(algo)
            #run end OK
            #bucle test
            #fitness = 0
            iosim = self.getConfig().getIO()
            fitness = 0
            for numTest in range(len(iosim.getInput())):
                if virMachine.runAlgorithm(iosim.getInput()[numTest]):
                    temp= self.fnFitness(virMachine.getMemory(),iosim.getOutput(),virMachine.getOutput(),virMachine.getResult())
                    fitness = fitness + temp
                else:
                    fitness = 0



    def getConfig(self):
        return self.config
    def run(self):
        print("Code run here")
        for generation in range(self.getConfig().getNumGenerations()):
            self.setCurrentGen(generation)
            print("Starting generation ",self.getCurrentGen())
            self.runSimAllAlgorithm()
    def setCurrentGen(self,s):
        self.currentGen = s
    def getCurrentGen(self):
        return self.currentGen
    def showResults(self):
        print("###############################")
        print("########### Results ###########")
        print("###############################")

    def welcomeMessage(self):
        print("################################################")
        print("####### Welcome to Evolutionary Algorithm ######")
        print("#######    Created by Anis Khoury Ribas   ######")
        print("################################################")
