# -*- coding: utf-8 -*-
DEBUG = False

from EVA import *
from structure.io import *
from features import *
from structure.virtualmachine import *

def mySkeleton():
    c = 0
    elements = list()
    for i in range(4):
        j = Instruction()
        j.generateCode("PUSH "+str(i)+" 0")
        elements.append(j)
    result = Algorithm(instructions=elements)
    return result
def myFitness(param):
    mem = param["mem"]
    inputExperiment = param["input"]
    result = param["resultExpected"]
    try:
        if mem[0]/mem[1] >0:
            return 0
        if mem[2]/mem[3] > 0:
            return 0
        sumVector= (float(mem[0])/mem[1]*inputExperiment[0])+(float(mem[2])/mem[3]*inputExperiment[1])
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


logFile = "log.txt"
logging.basicConfig(filename=logFile, level=logging.INFO)



io = IO()

# io.addTest([172,71],"",0)
# io.addTest([165,68],"",0)
# io.addTest([186,132],"",1)
# io.addTest([171,120],"",1)
# io.addTest([168,98],"",1)
# io.addTest([154,48],"",0)
# io.addTest([162,57],"",0)
# io.addTest([163,56],"",0)
# io.addTest([184,131],"",1)
# io.addTest([170,102],"",1)
# io.addTest([171,113],"",1)


io.addTest([0.9247311828,0.5378787879],"",0)
io.addTest([0.8870967742,0.5151515152],"",0)
io.addTest([1,1],"",1)
io.addTest([0.9193548387,0.9090909091],"",1)
io.addTest([0.9032258065,0.7424242424],"",1)
io.addTest([0.8279569892,0.3636363636],"",0)
io.addTest([0.870967742,0.431818182],"",0)
io.addTest([0.876344086,0.424242424],"",0)
io.addTest([0.989247312,0.992424242],"",1)
io.addTest([0.913978495,0.772727273],"",1)
io.addTest([0.919354839,0.856060606],"",1)

# io.addTest([162,57],"",0)
# io.addTest([162,57],"",0)



configuration = EVAconfig(io, numGenerations=800, numVirtualMachines=1, typeCross=0, population=50)
simulation = EVA(configuration, fnFitness=myFitness,population=None,funcSkeleton=mySkeleton)
algorithm = simulation.run(success=0.99)
algorithm.algoToASM()
