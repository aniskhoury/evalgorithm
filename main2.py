DEBUG = True

from EVA import *
from structure.io import *
import logging
import math
from structure.virtualmachine import *

def myFitness(mem, output, result,simulOutput, simResult):
    score = 0
    # fer la comprovació desitjada
    diffSqrt = (simResult - result)**2
    return 1 / (1 + diffSqrt)

logFile = "log.txt"
logging.basicConfig(filename=logFile, level=logging.INFO)


i = []
a,b = Instruction(),Instruction()
a.generateCode("ADDarg 0")
b.generateCode("ADDarg 4")

i.append(a)
i.append(b)
a = Algorithm(instructions=i)

a.showInstructions()
virtualMach = VirtualMachine(memory=512)
virtualMach.loadAlgorithm(a)
virtualMach.runAlgorithm([5,7,8,9,10])
print(virtualMach.getResult())
