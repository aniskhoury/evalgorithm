# -*- coding: utf-8 -*-
DEBUG = False

from EVA import *
from structure.io import *
from features import *
from structure.virtualmachine import *

def mySkeleton():
    elements = list()
    for i in range(20):
        j = Instruction()
        c = random.randint(0,26800000)
        j.generateCode("PUSH "+str(i)+" "+str(c))
        elements.append(j)
    result = Algorithm(instructions=elements)
    return result
def myFitness(param):
    mem = param["mem"]
    x = param["input"]
    result = param["resultExpected"]
    try:
        sumVector= 0
        #calculate the 5 variables
        for i in range(7):
            #sumVector= (float(mem[0])/mem[7+i]*x[i])
            #sumVector += (1/float(mem[i])) * x[i]
            sumVector += float(str("0."+str(mem[i])+str(mem[7+i]))) * x[i]
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
#normalize text & clean illegal characters
def cleanText(text):
    result = text.lower()
    characters = {"à": "a",
                  "ä": "a",
                  "á": "a",
                  "è": "e",
                  "ë": "e",
                  "é": "e",
                  "í": "i",
                  "ì": "i",
                  "ï": "i",
                  "ä": "a",
                  "ó": "o",
                  "ö": "o",
                  "ò": "o",
                  "ù": "u",
                  "ü": "u",
                  "ú": "u",
                  ",": "",
                  ";": "",
                  ".": "",
                  "·": "",
                  "?": "",
                  "¿": "",
                  "=": "",
                  "-": "",
                  "%": "",
                  "$": "",
                  "'": "",
                  "(": "",
                  ")": "",
                  "φ": "",
                  "θ": "",
                  "—": "",
                  "[": "",
                  "]": "",
                  "\"": "",
                  "\\": "",
                  "/":  "",
                  "\n": "",
                  "ç":  ""
                  }
    for i in range(10):
        characters[str(i)] = ""
    for key,value in characters.items():
        result = result.replace(key,value)
    return result
def isVowel(t):
    if t not in ["a","e","i","o","u"]:
        return False
    return True
#normalize vector
def normalizeVectorT(vector,lenght):
    maxNorm = []
    normalizedVector = []
    for i in range(1,lenght+1):
        maxNorm.append(max([e[i] for e in vector]))
    for i in vector:
        tempList = []

        for element in range(lenght):
            tempList.append(float(i[element+1])/maxNorm[element])
        normalizedVector.append(tempList)

    return normalizedVector
#genera el vector de dades training per la simulacio
#Les variables son les definides al model 1
def generateVectorTmodel1(data):
    words = data.split(" ")
    vectorX = []
    for word in words:
        if len(word) < 1:
            continue
        startVowel = int(isVowel(word[0]))
        endVowel = int(isVowel(word[len(word)-1]))
        numVowel = 0
        numConsonant = 0
        lenghtWord = 0
        for character in word:
            if isVowel((character)):
                numVowel += 1
            else:
                numConsonant += 1
            lenghtWord += 1
        vectorX.append([word,startVowel,endVowel,numVowel,numConsonant,lenghtWord])
    return vectorX
#genera el vector de dades training per la simulacio
#Les variables son les definides al model 2
def generateVectorTmodel2(data):
    words = data.split(" ")
    vectorX = []
    for word in words:
        if len(word) < 1:
            continue
        startVowel = int(isVowel(word[0]))
        endVowel = int(isVowel(word[len(word)-1]))
        numVowel = 0
        numConsonant = 0
        lenghtWord = 0
        numDoubleVowel = 0
        numDoubleConsonant = 0
        for character in range(len(word)):
            if isVowel((word[character])):
                numVowel += 1
                try:
                    if isVowel(word[character+1]):
                        numDoubleVowel += 1
                except IndexError:
                    continue
            else:
                numConsonant += 1
                try:
                    if isConstant(word[character+1]):
                        numDoubleConsonant += 1
                except IndexError:
                    continue
            lenghtWord += 1
        vectorX.append([word,startVowel,endVowel,numVowel,numConsonant,
                       lenghtWord,numDoubleVowel,numDoubleConsonant])
    return vectorX
def startVowel(t):
    return isVowel(t[0])


#detect english & catalan text
catalaWords = open('catala.txt').read()
englishWords = open('english.txt').read()
spanishWords = open('spanish.txt').read()

cleanCatala = cleanText(catalaWords)
cleanEnglish = cleanText(englishWords)
cleanSpanish = cleanText(spanishWords)

############################################################################
## Generació dels vectors caraceristics pels models definits a la memoria ##
############################################################################

#vector caracteristiques del model 1 (5 variables)
vectorCatala1  = generateVectorTmodel1(cleanCatala)
vectorEnglish1 = generateVectorTmodel1(cleanEnglish)
vectorSpanish1 = generateVectorTmodel1(spanishWords)

#vector caracteristiques del model 2 (7 variables)
vectorCatala2  = generateVectorTmodel2(cleanCatala)
vectorEnglish2 = generateVectorTmodel2(cleanEnglish)
vectorSpanish2 = generateVectorTmodel2(spanishWords)

#vector caracteristiques del model 2 (32 variables)
#vectorCatala3  = generateVectorTmodel3(cleanCatala)
#vectorEnglish3 = generateVectorTmodel3(cleanEnglish)
#vectorSpanish3 = generateVectorTmodel3(spanishWords)


###############################################################################
## normalitzacio de valors del vector x (per trobar w de l'equació x*w-b>=1) ##
###############################################################################

#normalitzacio de valors del vector x (per trobar w de l'equació x*w-b>=1)
#Model 1
vectorNormCat1 =  normalizeVectorT(vectorCatala1,5)
vectorNormEng1 = normalizeVectorT(vectorEnglish1,5)
vectorNormSpa1 = normalizeVectorT(vectorSpanish1,5)

#normalitzacio de valors del vector x (per trobar w de l'equació x*w-b>=1)
#Model 2
vectorNormCat2 =  normalizeVectorT(vectorCatala2,7)
vectorNormEng2 = normalizeVectorT(vectorEnglish2,7)
vectorNormSpa2 = normalizeVectorT(vectorSpanish2,7)

io = IO()
#Assignem una categoria a les dades a classificar
#Català -> category 0
#Totes les demes 1
for element in vectorNormCat2:
    io.addTest(element,"",0)
for element in vectorNormEng2:
    io.addTest(element, "", 1)
for element in vectorNormSpa2:
    io.addTest(element, "", 1)

configuration = EVAconfig(io, numGenerations=1000, numVirtualMachines=1, typeCross=0, population=50)
simulation = EVA(configuration, fnFitness=myFitness,population=None,funcSkeleton=mySkeleton)
simulation.run(success=0.70)
simulation.showResults()
simulation.showBest()
bestAlgorithm = simulation.getBest()

#vector caracteristic per testejar.
#dadesEntradaTest = []
#virM= VirtualMachine(memory=64)
#virM.loadAlgorithm(bestAlgorithm)
#virM.runAlgorithm(dadesEntradaTest)