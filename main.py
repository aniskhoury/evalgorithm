DEBUG = True

from EVA import *
from structure.io import *
import logging
from structure.virtualmachine import *

def myFitness(mem, output, simulOutput, simResult):
    score = 0
    # fer la comprovació desitjada
    return 1 / (1 + (score))

logFile = "log.txt"
logging.basicConfig(filename=logFile, level=logging.INFO)

# io = IO()
# io.addTest([5, 10, 15, 20],"15",15)
# io.addTest([4,9,14,19],"14",14)
# configuration = EVAconfig(io, numGenerations=500, numVirtualMachines=1, typeCross=0, population=100)
# simulation = EVA(configuration, fnFitness=myFitness)
# #simulation.init()  # Optatiu simulation.init(Population=la_poblacio_dessitjada_per_repetir_experiment)
# simulation.run()
# simulation.showResults()
#addi 4
al = Algorithm(instructions = [Instruction(code="00001000000000000000000000000110")])
virtualMach = VirtualMachine(memory=512)
virtualMach.loadAlgorithm(al)
virtualMach.runAlgorithm([5, 10, 15, 20])
print(virtualMach.getResult())


