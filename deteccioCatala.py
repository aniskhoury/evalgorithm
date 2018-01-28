# -*- coding: utf-8 -*-
DEBUG = False

from EVA import *
from structure.io import *
from features import *
from structure.virtualmachine import *

def mySkeleton():
    c = 0
    elements = list()
    #8 elements of feature vector + bypass
    #We duplicate the element for concatenate float in fitness function
    for i in range((8*2)+1):
        j = Instruction()
        j.generateCode("PUSH "+str(i)+" "+str(random.randint(0,9000)))
        elements.append(j)
    result = Algorithm(instructions=elements)
    return result
def myFitness(param):
    mem = param["mem"]
    inputExperiment = param["input"]
    result = param["resultExpected"]
    try:
        b = mem[8]
        sumVector = sum([ (float(mem[i*2])/mem[(i*2)+1])*inputExperiment[0] for i in range(8)])

        #cas grup x*pes >=1
        if result == 1:
            if sumVector >=1:
                return 1
            else:
                return 0
        else:
            if sumVector <1:
                return 1
            else:
                return 0

    except ZeroDivisionError:
        return 0


cat = getCatDiccionary(250)
cast = getCastDiccionary(250)
eng = getEnglDiccionary(50)
vectorFeatures = getVectorFeatureCat(cat)
io = IO()

###########################
# Prepare training vector #
###########################
#Catalan expected result "1"
#Other languages, result "0"
#catalan case
for element in getVectorFeatureCat(cat):
    io.addTest(element[0],"",1)
#castella case
for element in getVectorFeatureCat(cast):
    io.addTest(element[0],"",0)
# #english case
# for element in getVectorFeatureCat(eng):
#     io.addTest(element[0],"",0)

# io.addTest([162,57],"",0)
# io.addTest([162,57],"",0)



configuration = EVAconfig(io, numGenerations=800, numVirtualMachines=1, typeCross=0, population=100)
simulation = EVA(configuration, fnFitness=myFitness,population=None,funcSkeleton=mySkeleton)
algorithm = simulation.run(success=0.99,mutationProb=5)
algorithm.algoToASM()



testParaula()
