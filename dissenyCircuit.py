# -*- coding: utf-8 -*-

DEBUG = False

from EVA import *
from structure.io import *
from features import *
from structure.virtualmachine import *
def mySkeleton():
    ins = [Instruction() for i in range(4)]

    ins[0].generateCode("PUTmemarg 5 1")
    ins[1].generateCode("PUTmemarg 6 0")
    ins[2].generateCode("ANDmem 0 5 6")
    ins[3].generateCode("XORmem 1 5 20")

    result = Algorithm(instructions=ins)
    return result


def myFitness(param):
    mem = param["mem"]
    input = param["input"]
    result = param["resultExpected"]

    try:
        c = 0
        formula = 0.0
        while c < 13:
            formula =  formula +float(mem[c]*input[c]+mem[15+c])
            c += 1
        #if is catalan, 1 is expected. Then we have to check
        # sum(vector of w*x+b) > 1
        #else sum(vector of w*x+b) < 1
        #formula = mem[0]*testInput[0]+mem[2]
        #formula = formula + ((mem[1] * testInput[1]) + mem[2])

        if result == 1:
            if formula < 1:
                return 1
        else:
            if formula > 1:
                return 1
        return 0

    except ZeroDivisionError:
        return 0


# #simulation.init()  # Optatiu simulation.init(Population=la_poblacio_dessitjada_per_repetir_experiment)
# simulation.run()
# simulation.showResults()

def getMax(vector,indexFeature):
    return float(max(vector[:][indexFeature]))
def normalize(vector):
    col = len(vector[0])
    maxValues = [getMax(vector,i) for i in range(13)]
    maxValues.append(1)
    for i in range(len(vector)):
        for j in range(col):
            vector[i][j] = vector[i][j]/maxValues[j]


def fitCircuit(param):
    memoria = param["mem"]
    sortidaEsperada = param["resultExpected"]

    if (memoria[0] == sortidaEsperada[0]) and (memoria[1] == sortidaEsperada[1]):
        return 1  # El resultat esperat es equivalent al trobat per l’algorisme
    return 0  # El resultat de la simulació de l’algorisme no coincideix amb la Y esperada


training = IO()
#Dades d'entrenament. Taula de la veritat operació Suma amb Carry
training.addTest([0,0],"",[0,0])
training.addTest([0,1],"",[0,1])
training.addTest([1,0],"",[0,1])
training.addTest([1,1],"",[1,0])



configuration = EVAconfig(training, numGenerations=500000, numVirtualMachines=1, typeCross=0, population=50)
simulation = EVA(configuration, fnFitness=fitCircuit,population=None,funcSkeleton=mySkeleton)
algorithm = simulation.run(success=0.9,mutationProb=5)
algorithm.algoToASM()




