
from structure.virtualmachine import *
from structure.evaconfig import *
from structure.population import *
from operator import attrgetter

import math

DEBUG = True
class EVA:
    virtualMachines = []
    config = None
    currentGen = 0
    population = None
    fnFitness = None
    fnCross = None

    def __init__(self,config,virtualMachines=None,fnFitness=None,fnCross=None,population=None):
        self.setConfig(config)
        self.createVirtualMachine(n=1)
        self.welcomeMessage()
        if population == None:
            self.population = Population()
            self.population.createPopulation(config)
        else:
            self.setPopulation(population)
        #self.population.showPopulation()

        if fnFitness == None:
            self.fnFitness = self.funcFitness()
        else:
            self.fnFitness = fnFitness
        if fnCross == None:
            self.fnCross = self.funcCross()
        else:
            self.fnCross = fnCross
    def getPopulation(self):
        return self.population
    def setPopulation(self,s):
        self.population = s
    def setConfig(self,c):
        self.config = c
    #n -> Number of virtual machines created.
    def funcCross(self):
        return 0
    def funcFitness(self,mem, output, result,simulOutput, simResult):
        score = 0
        # fer la comprovacio desitjada
        diffSqrt = math.sqrt(simResult ** 2 - result ** 2) ** 2
        return 1 / (1 + diffSqrt)
    def createVirtualMachine(self,n=1):
        self.virtualMachines.append(VirtualMachine(memory=4096*32))
    def getVirtualMachines(self):
        return self.virtualMachines
    def getPopulation(self):
        return self.population
    def getBest(self):
        return self.getPopulation().getElements()[0].getAlgorithm()

    def runSimAllAlgorithm(self):
        virMachine = self.getVirtualMachines()[0]
        iosim = self.getConfig().getIO()
        popu = self.getPopulation()

        for element in range(len(popu.getElements())):

            #Algorithm was stored in elementPopulation
            algo = self.getPopulation().getElements()[element].getAlgorithm()
            virMachine.loadAlgorithm(algo)
            fitness = 0.0
            c = 0

            for testInput in iosim.getInput():
                virMachine.resetRun()
                virMachine.resetTest()
                if virMachine.runAlgorithm(testInput):
                    mem = virMachine.getMemory()
                    resu = float(self.config.getIO().getResult()[c])
                    outputTest = str(iosim.getOutput()[c])
                    outputVir= str(self.getVirtualMachines()[0].getOutput())
                    resultVir= float(self.getVirtualMachines()[0].getResult())
                    temp= self.fnFitness(mem,outputTest,resu,outputVir,resultVir)
                    fitness = fitness + temp
                    c = c +1
                else:
                    fitness = -1
                    break

            if fitness == -1:
                self.getPopulation().getElements()[element].setScore(-1)
            else:
                self.getPopulation().getElements()[element].setScore(fitness/len(iosim.getInput()))
    def showBest(self):
        print("Best:")
        self.getPopulation().getElements()[0].showElement()
        print("Code ASM")
        self.getPopulation().getElements()[0].getAlgorithm().algoToASM()
    def showAllPopulation(self):
        print("#################################")
        print("######## Show Population ########")
        print("#################################")
        popu = self.getPopulation().showAll()


    def getConfig(self):
        return self.config
    def orderPopu(self):
        popu = self.getPopulation().getElements()
        orderedPopu = sorted(popu,key=attrgetter('score'),reverse=True)
        self.setPopulation(Population(population=orderedPopu))


    def nextPopulation(self):
        oldPopu = self.getPopulation().getElements()

        popu = Population()
        popu.addElementPopu(oldPopu[0])
        numAlgorithms = self.getConfig().getPopulation()
        for i in range(numAlgorithms-1):
            indexAlgo1 = random.randint(0,numAlgorithms-1)
            indexAlgo2 = random.randint(0,numAlgorithms-1)
            child = oldPopu[indexAlgo1].getAlgorithm().cross(oldPopu[indexAlgo2].getAlgorithm())
            popu.addElementPopu(elementPopulation(algorithm=child))
        self.setPopulation(popu)
    def getBest(self):
        return self.getPopulation().getElements()[0]
    def run(self):
        for generation in range(self.getConfig().getNumGenerations()):
            self.setCurrentGen(generation)
            print("Starting generation ",self.getCurrentGen())
            self.runSimAllAlgorithm()
            #order by score
            self.orderPopu()
            if self.getBest().getScore() == 1:
                return
            self.nextPopulation()

            #choose accurate fitness value and stop if it pass
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
