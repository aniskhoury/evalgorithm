# -*- coding: utf-8 -*-

DEBUG = False

from EVA import *
from structure.io import *
from features import *
from structure.virtualmachine import *
def mySkeleton():
    ins = [Instruction() for i in range(10)]

    ins[0].generateCode("PUTmemarg 0 1")
    ins[1].generateCode("PUTmemarg 1 1")
    ins[2].generateCode("ANDmem 2 1 0")
    ins[3].generateCode("NOTmem 2 2")

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

io = IO()
def fitCircuit(param):
    mem = param["mem"]
    input = param["input"]
    result = param["resultExpected"]
    #print mem,result,input
    #print type(mem[2]),type(result)
    if mem[2] == result:  # el resultat de 0x0002 correspon a la Y de la taula veritat?
        return 1  # El resultat esperat es equivalent al trobat per l’algorisme
    return 0  # El resultat de la simulació de l’algorisme no coincideix amb la Y esperada


#for i in getAllFeatures():
#    io.addTest(i[:-1], "", i[8])
#poblacio 0-> alt i gras
#poblacio 1-> alt i prim
#poblacio 2-> baix i gordo
#poblacio 3-> baix i prim


#io.addTest([20,5,6,8],"",20)
io.addTest([0,0],"",1)
io.addTest([0,1],"",1)
io.addTest([1,0],"",1)
io.addTest([1,1],"",0)



configuration = EVAconfig(io, numGenerations=800, numVirtualMachines=1, typeCross=0, population=50)
simulation = EVA(configuration, fnFitness=fitCircuit,population=None,funcSkeleton=mySkeleton)
algorithm = simulation.run(success=0.95)
algorithm.algoToASM()