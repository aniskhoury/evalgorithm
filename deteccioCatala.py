# -*- coding: utf-8 -*-
DEBUG = False

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
    for i in range(50+1):
        j = Instruction()
        j.generateCode("PUSH "+str(i)+" "+str(random.randint(0,9000)))
        elements.append(j)
    result = Algorithm(instructions=elements)
    return result
def myFitness(param):
    mem = param["mem"]
    x = param["input"]
    result = param["resultExpected"]
    try:
        #sumVector = sum([ (float(mem[i*2])/mem[(i*2)+1])*inputExperiment[0] for i in range(8)])
        #sumVector = sum([float(str("0."+str(mem[i]))) for i in range(50)]])
        sumVector = 0.0
        #number of features:50
        #mem[50] = b
        #Formula: sumatori x*w-b
        for w in range(50):
            sumVector = sumVector + ((float(str("0.") + str(mem[w]))*x[w])-mem[50])

        #for w in range(50):
        #    sumVector = sumVector + ((mem[w*2]/mem[(w*2)+1])*x[w])

        #cas grup x*pes >=1
        if result == 1:
            if sumVector >=0.5:
                return 1
            return 0
        else:
            if sumVector <1:
                return 1
            return 0

    except ZeroDivisionError:
        return 0

wordsCat = open("catala.txt").read()
wordsAng = open("angles.txt").read()
wordsEus = open("euscar.txt").read()
wordsCast = open("castella.txt").read()

catalaFeatureVector   = generateAllVectorFeature(wordsCat,vowelList,punctuationList,grafemes)
anglesFeatureVector   = generateAllVectorFeature(wordsAng,vowelList,punctuationList,grafemes)
euscarFeatureVector   = generateAllVectorFeature(wordsEus,vowelList,punctuationList,grafemes)
castellaFeatureVector = generateAllVectorFeature(wordsCat,vowelList,punctuationList,grafemes)

io = IO()

###########################
# Prepare training vector #
###########################
#Catalan expected result "1"
#Other languages, result "0"
#catalan case
for element in catalaFeatureVector:
    io.addTest(element,"",1)
#angles case
for element in anglesFeatureVector:
    io.addTest(element,"",0)
#euscar case
for element in castellaFeatureVector:
    io.addTest(element,"",0)
#castella case
for element in castellaFeatureVector:
    io.addTest(element,"",0)

configuration = EVAconfig(io, numGenerations=200, numVirtualMachines=1, typeCross=0, population=30)
simulation = EVA(configuration, fnFitness=myFitness,population=None,funcSkeleton=mySkeleton)
algorithm = simulation.run(success=1.0,mutationProb=5)
#algorithm.algoToASM()
VM = VirtualMachine(128)
VM.loadAlgorithm(algorithm)
#run without parameters
VM.runAlgorithm([])
print(VM.getMemory())
#weights = getVectorCriature(VM.getMemory(),50)
weights = [0, 0, 0, 0, 0, 264, 8126, 4970, 1783, 2612, 1928, 6373, 0, 0, 0, 1383, 0, 5294, 6405, 0, 0, 0, 0, 0, 1067, 7187, 0, 4142, 6744, 6092, 1701, 3110, 2026, 2016, 2120, 7891, 0, 0, 0, 0, 0, 0, 3536, 4277, 0, 0, 4746, 615, 0, 0, 0, 0, 248, 0, 0, 0, 1398, 0, 0, 0, 7383, 0, 0, 4319, 0, 7294, 0, 1151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7487, 0, 1099, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def testWord(vectorW,x,grafemes,vowelList,punctuationList):

    sumVector = 0.0

    for w in range(len(vectorW)):
        sumVector = sumVector + (vectorW[w] * x[w])
    return sumVector
def testText(vectorW,text,grafemes,vowelList,punctuationList):
    t = text.split()

    numWordCat = 0
    numWordNoCat = 0
    print(t)
    for nWord in range(len(t)):
        x = generateVectorFeatureWord(t[nWord], vowelList, punctuationList, grafemes)
        x = normalizeVectorFeature(x)
        result = testWord(vectorW,x, vowelList, punctuationList, grafemes)
        if result >=1:
            numWordCat = numWordCat+1
        else:
            numWordNoCat = numWordNoCat+1
        print(result)
    print("Text en català")
    print("Numeros paraules detectades en catala",numWordCat)
    print("Numeros paraules no detectades en catala",numWordNoCat)

text = "L'univers és la totalitat del continu espaitemps en què es troba la humanitat, juntament amb tota la matèria i energia que conté. A gran escala, és l'objecte d'estudi de la cosmologia, que es basa en la física i l'astronomia, tot i que alguns dels temes d'estudi voregen la metafísica. Actualment, els experts no estan d'acord sobre si és possible (en principi) d'arribar a observar la totalitat de l'univers.".decode('utf-8').replace(" ","")
#x = generateVectorFeatureWord(text, vowelList, punctuationList, grafemes)

#result = testWord(weights,x, vowelList, punctuationList, grafemes)

#text = "hola como estais yo muy bien espero que vosotros también".decode('utf-8')

testText(weights,text,grafemes,vowelList,punctuationList)

