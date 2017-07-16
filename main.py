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


# #simulation.init()  # Optatiu simulation.init(Population=la_poblacio_dessitjada_per_repetir_experiment)
# simulation.run()
# simulation.showResults()
#addi 4
i = []
a = Instruction()
a.generateCode("ADDarg 0")
i.append(a)
a.showInfo()
b = Instruction()

b.generateCode("ADDarg 1")
i.append(b)
b.showInfo()
al = Algorithm(instructions = i)
io = IO()
io.addTest([5, 10, 15, 20],"15",15)
io.addTest([4,9,14,19],"13",13)
pop = Population()
pop.addElementPopu(elementPopulation(al))
configuration = EVAconfig(io, numGenerations=5, numVirtualMachines=1, typeCross=0, population=100)
simulation = EVA(configuration, fnFitness=myFitness,population=pop)
simulation.run()
simulation.showResults()
simulation.showAllPopulation()



#
#
# virtualMach = VirtualMachine(memory=512)
# virtualMach.loadAlgorithm(al)
# if virtualMach.runAlgorithm([5, 10, 15, 20]) == False:
#     print("Error algorithm")
# else:
#     print(virtualMach.getResult())


