DEBUG = True

from EVA import *
from structure.io import *
import logging
import math
from structure.virtualmachine import *

def myFitness(mem, output, result,simulOutput, simResult):
    try:
        print("mem1",mem[1])
        print("mem2",mem[2])
        resulAlgoritme =  mem[1]/mem[2]
        diffSqrt =  (result - resulAlgoritme)**2
        return 1/(1 + diffSqrt)
    except ZeroDivisionError:
        return 0


logFile = "log.txt"
logging.basicConfig(filename=logFile, level=logging.INFO)


# #simulation.init()  # Optatiu simulation.init(Population=la_poblacio_dessitjada_per_repetir_experiment)
# simulation.run()
# simulation.showResults()
#addi 4
def genInstruction(txt):
    a = Instruction()
    a.generateCode(txt)
    return a
i = []
a = Instruction()
i.append(genInstruction("PUSH 1 5"))
i.append(genInstruction("PUSH 2 5"))
i.append(genInstruction("PUSH 3 5"))


al = Algorithm(instructions = i)
al.showInstructions()
io = IO()


io.addTest([20,5,6,8],"",20)

configuration = EVAconfig(io, numGenerations=1000, numVirtualMachines=1, typeCross=0, population=100)
simulation = EVA(configuration, fnFitness=myFitness)
simulation.run()
simulation.showResults()
simulation.showBest()
