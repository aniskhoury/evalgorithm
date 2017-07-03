from EVA import *
import logging

def myFitness(mem, output, simulOutput, simResult):
    score = 0
    # fer la comprovació desitjada
    return 1 / (1 + (score))

logFile = "log.txt"
logging.basicConfig(filename=logFile, level=logging.INFO)

io = IO()
io.input([DadaTest0, DadaTest1, DadaTest2, DadaTest3....])
io.output([OutputEsperat0, OutputEsperat1, OutputEsperat2...])
io.result(0)
configuration = EVAconfig(io, numGeneration=2000, numVirtualMachines=1, typeCross=0, population=100....)
simulation = EVA(configuration, fnFitness=myFitness)
simulation.init()  # Optatiu simulation.init(Population=la_poblacio_dessitjada_per_repetir_experiment)
simulation.run()
simulation.showResults()