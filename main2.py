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
b.generateCode("ADDarg 1")

i.append(a)
i.append(b)
a = Algorithm(instructions=i)
b = Algorithm(instructions=i)
c = a.cross(b)
c.showInstructions()

