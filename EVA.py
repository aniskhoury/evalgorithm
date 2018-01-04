
from structure.virtualmachine import *
from structure.evaconfig import *
from structure.population import *
from operator import attrgetter

import math

DEBUG = False
class EVA:
    virtualMachines = []
    config = None
    currentGen = 0
    population = None
    fnFitness = None
    fnCross = None
    fnSkeleton = None
    def __init__(self,config,virtualMachines=None,fnFitness=None,fnCross=None,population=None,funcSkeleton=None):
        self.setConfig(config)
        self.createVirtualMachine(n=1)
        self.welcomeMessage()
        if population == None:
            self.population = Population(fnskeleton=funcSkeleton)
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
    def createVirtualMachine(self,n=1,memory=64):
        for i in range(n):
            self.virtualMachines.append(VirtualMachine(memory))
    def getVirtualMachines(self):
        return self.virtualMachines
    def getPopulation(self):
        return self.population
    def getBest(self):
        return self.getPopulation().getElements()[0].getAlgorithm()
    def runSimAllAlgorithm(self,success=0.7):
        virMachine = self.getVirtualMachines()[0]
        iosim = self.getConfig().getIO()
        popu = self.getPopulation()
        fitness = 0.0
        for element in range(len(popu.getElements())):
            #Algorithm was stored in elementPopulation
            algo = self.getPopulation().getElements()[element].getAlgorithm()
            virMachine.loadAlgorithm(algo)
            fitness = 0.0
            totalTest = len(iosim.getInput())
            #for n in range(totalTest):
            c = 0
            for i in iosim.getInput():
                virMachine.resetRun()
                virMachine.resetTest()
                virMachine.runAlgorithm(i)
                param = {}
                param["mem"] = virMachine.getMemory()
                param["resultExpected"] =  iosim.getResult()[c]
                param["outputExpected"] =  iosim.getOutput()[c]
                param["input"] = i

                param["output"] =  str(self.getVirtualMachines()[0].getOutput())
                param["resultVir"] =  float(self.getVirtualMachines()[0].getResult())
                param["algorithm"] = algo
                c = c+1

                temp= self.fnFitness(param)

                fitness = fitness + temp

            try:
                self.getPopulation().getElements()[element].setScore(fitness/c)
            except ZeroDivisionError:
                self.getPopulation().getElements()[element].setScore(0.0)
    def showBest(self):
        print("Best:")
        #self.getPopulation().getElements()[0].showElement()
        print("Code ASM")
        print self.getBest().algoToASM()
    def showAllPopulation(self):
        print("#################################")
        print("######## Show Population ########")
        print("#################################")
        popu = self.getPopulation().showAll()
    def getBestAlgorithm(self):
        return self.getPopulation().getElements()[0].getAlgorithm()

    def getConfig(self):
        return self.config
    def orderPopu(self):
        popu = self.getPopulation().getElements()
        orderedPopu = sorted(popu,key=attrgetter('score'),reverse=True)
        self.setPopulation(Population(population=orderedPopu))
    def showPopuScore(self):
        popu = self.getPopulation().getElements()
        for i in popu:
            i.getAlgorithm().algoToASM()
            print "score---->",i.getScore()
    def nextPopulation(self):
        oldPopu = self.getPopulation().getElements()

        popu = Population()
        #save always the best criature
        popu.addElementPopu(oldPopu[0])
        numAlgorithms = self.getConfig().getPopulation()
        for i in range(numAlgorithms-1):
            indexAlgo1 = random.randint(0,numAlgorithms-1)
            indexAlgo2 = random.randint(0,numAlgorithms-1)
            child = oldPopu[0].getAlgorithm().cross(oldPopu[indexAlgo2].getAlgorithm())
            popu.addElementPopu(elementPopulation(algorithm=child))
        self.setPopulation(popu)
    def getBest(self):
        return self.getPopulation().getElements()[0]
    def run(self,success=0.7):
        for generation in range(self.getConfig().getNumGenerations()):
            self.setCurrentGen(generation)
            print("Starting generation ",self.getCurrentGen())
            self.runSimAllAlgorithm(success=success)
            self.orderPopu()
            #self.showPopuScore()
            #order by score
            bestScore = self.getBest().getScore()
            self.runSimAllAlgorithm(success=success)
            print("Actual best score:", self.getBest().getScore())
            self.getBest().getAlgorithm().algoToASM()
            if self.getBest().getScore() >=success:
                print("Found solution with score",self.getBest().getScore())
                return self.getBest().getAlgorithm()
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
