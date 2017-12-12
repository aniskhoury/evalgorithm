# -*- coding: utf-8 -*-
DEBUG = False

from EVA import *
from structure.io import *
from features import *
from structure.virtualmachine import *

def mySkeleton():
    c = 0
    elements = list()
    for i in range(10):
        j = Instruction()
        j.generateCode("PUSH "+str(i)+" 0")
        elements.append(j)
    result = Algorithm(instructions=elements)
    return result
def myFitness(param):
    mem = param["mem"]
    inputExperiment = param["input"]
    result = param["resultExpected"]
    try:
        sumVector= 0
        #calculate the 5 variables
        for i in range(5):
            sumVector= (float(mem[0])/mem[(i*2)+1]*inputExperiment[i])
            #sumVector += (1/float(mem[i])) * inputExperiment[i]
            #sumVector += float(str("0."+str(mem[i]))) * inputExperiment[i]
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
def normalizeVectorT(vector):
    maxNorm = []
    normalizedVector = []
    for i in range(1,6):
        maxNorm.append(max([e[i] for e in vector]))
    for i in vector:
        tempList = []

        for element in range(5):
            tempList.append(float(i[element+1])/maxNorm[element])
        normalizedVector.append(tempList)

    return normalizedVector
#generateVectorTest
def generateVectorTmodel1(data):
    words = data.split(" ")
    vector = []
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
        vector.append([word,startVowel,endVowel,numVowel,numConsonant,lenghtWord])
    return vector
def startVowel(t):
    return isVowel(t[0])

#detect english & catalan text
catalaWords = open('catala.txt').read()
englishWords = open('english.txt').read()

cleanCatala = cleanText(catalaWords)
cleanEnglish = cleanText(englishWords)
vectorCatala= generateVectorTmodel1(cleanCatala)
vectorEnglish= generateVectorTmodel1(cleanEnglish)
vectorNormCat =  normalizeVectorT(vectorCatala)
vectorNormEng = normalizeVectorT(vectorEnglish)

io = IO()
#Català -> category 0
for element in vectorNormCat:
    io.addTest(element,"",0)
for element in vectorNormEng:
    io.addTest(element, "", 1)

# io.addTest([172,71],"",0)
# io.addTest([165,68],"",0)
# io.addTest([186,132],"",1)
# io.addTest([171,120],"",1)
# io.addTest([168,98],"",1)
# io.addTest([154,48],"",0)
# io.addTest([162,57],"",0)
# io.addTest([163,56],"",0)
# io.addTest([184,131],"",1)
# io.addTest([170,102],"",1)
# io.addTest([171,113],"",1)



# io.addTest([162,57],"",0)
# io.addTest([162,57],"",0)


configuration = EVAconfig(io, numGenerations=1000, numVirtualMachines=1, typeCross=0, population=50)
simulation = EVA(configuration, fnFitness=myFitness,population=None,funcSkeleton=mySkeleton)
simulation.run(success=0.9)
simulation.showResults()
simulation.showBest()
