# -*- coding: utf-8 -*-

from EVA import *
from structure.io import *
from features import *
from structure.virtualmachine import *

def getVectorCriature(memory,nFeatures):
    wFeatures = []
    for n in range(nFeatures):
        wFeatures.append(float("0."+str(memory[n])))
    return wFeatures

def mySkeleton():
    c = 0
    elements = list()
    #8 elements of feature vector + bypass
    #We duplicate the element for concatenate float in fitness function
    for i in range(4):
        j = Instruction()
        j.generateCode("PUSH "+str(i)+" "+str(random.randint(0,90)))
        elements.append(j)
    result = Algorithm(instructions=elements)
    return result
def myFitness(param):
    mem = param["mem"]
    x = param["input"]
    result = param["resultExpected"]
    c = 0
    prediccio = 0.0
    b = mem[3]


    while c < 3:
            #s'aplica el sumatori de x*w-b
            prediccio = prediccio + (float("0."+str(mem[c])) * x[c] + b)
            c += 1

    #El cas de "te taquicardia"
    if result == 1:
        if prediccio > 1: #la prediccio ha encertat que te taquicardia?
            return 1
    #cas no te taquicardia
    else:
        if prediccio < 1: #la prediccio ha encertat que no te taquicardia?
            return 1
    return 0


def comprovarTaquicardia(cEdat,cBatecs):
    teTaquicardia = 0
    #S'ha utilitzat la taula explicada a la memoria per comprovar si s'està davant
    #d'una taquicardia o no

    if cEdat == 1 and cEdat <2:
        if cBatecs > 169:
            teTaquicardia = 1
    if cEdat > 1 and cBatecs < 3:
        if cBatecs > 151:
            teTaquicardia = 1
    if cEdat > 3 and cBatecs < 8:
        if cBatecs > 137:
            teTaquicardia = 1
    if cEdat > 8 and cBatecs < 11:
        if cBatecs > 130:
            teTaquicardia = 1
    if cEdat > 11 and cBatecs < 15:
        if cBatecs > 119:
            teTaquicardia = 1
    if cEdat > 11 and cBatecs < 15:
        if cBatecs > 119:
            teTaquicardia = 1
    if cEdat >= 15 and cBatecs > 100 :
        teTaquicardia = 1
    return teTaquicardia
def normal(vector):
    vNorm = []
    maxValor = max(vector)*1.0
    for element in vector:
        vNorm.append(element/maxValor)
    return vNorm
def dataTraining(N=200):
    vTraining = []

    c = 0
    while c < N:

        cBatecs = random.randint(20, 240)
        cSegons = 60
        cEdat = random.randint(1,90)
        teTaquicardia = comprovarTaquicardia(cEdat,cBatecs)
        v = [cBatecs,cEdat,cSegons]

        #normalitzacio del vector
        v = normal(v)
        v = v + [teTaquicardia]

        #afegeix el vector d'entrenament a la llista de vectors que servira
        #per entrenar la SVM
        vTraining.append(v)
        c = c+1
    return vTraining



training = IO()
#Dades d'entrenament. Taula de la veritat operació Suma amb Carry
vEntrenament = dataTraining(N=120)

for i in vEntrenament:
    training.addTest([i[0],i[1],i[2]],"",i[3])




configuration = EVAconfig(training, numGenerations=500000, numVirtualMachines=1, typeCross=0, population=50)
simulation = EVA(configuration, fnFitness=myFitness,population=None,funcSkeleton=mySkeleton)
algorithm = simulation.run(success=1.0,mutationProb=8)
algorithm.algoToASM()
