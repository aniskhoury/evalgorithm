DEBUG = True

from EVA import *
from structure.io import *
from features import *
from structure.virtualmachine import *

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
for i in getAllFeatures():
    io.addTest(i[:-1], "", i[8])
#poblacio 0-> alt i gras
#poblacio 1-> alt i prim
#poblacio 2-> baix i gordo
#poblacio 3-> baix i prim


#io.addTest([20,5,6,8],"",20)

configuration = EVAconfig(io, numGenerations=1000, numVirtualMachines=1, typeCross=0, population=50)
simulation = EVA(configuration, fnFitness=myFitness,population=None)
simulation.run(success=0.98)
simulation.showResults()
simulation.showBest()
