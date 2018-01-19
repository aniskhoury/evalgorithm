# -*- coding: utf-8 -*-
import itertools
import random
english = "Directed evolution is a method used in protein engineering that mimics the process of natural selection to evolve proteins or nucleic acids toward a user-defined goal. It consists of subjecting a gene to iterative rounds of mutagenesis (creating a library of variants), selection (expressing the variants and isolating members with the desired function), and amplification (generating a template for the next round). It can be performed in vivo (in living cells), or in vitro (free in solution or microdroplet). Directed evolution is used both for protein engineering as an alternative to rationally designing modified proteins, as well as studies of fundamental evolutionary principles in a controlled, laboratory environment. Combined, 'semi-rational' approaches are being investigated to address the limitations of both rational design and directed evolution. Beneficial mutations are rare, so large numbers of random mutants have to be screened to find improved variants. 'Focussed libraries' concentrate on randomising regions thought to be richer in beneficial mutations for the mutagenesis step of DE. A focussed library contains fewer variants than a traditional random mutagenesis library and so does not require such high-throughput screening. These gas-like ions rapidly interact with ions of opposite charge to give neutral molecules or ionic salts. Ions are also produced in the liquid or solid state when salts interact with solvents (for example, water) to produce solvated ions, which are more stable, for reasons involving a combination of energy and entropy changes as the ions move away from each other to interact with the liquid. These stabilized species are more commonly found in the environment at low temperatures. A common example is the ions present in seawater, which are derived from the dissolved salts."


catala = "L'evolució dirigida és un mètode utilitzat en l'enginyeria de proteïnes per aprofitar el poder de la selecció natural i obtenir proteïnes o ARN amb les propietats desitjades que no es troben a la natura- Un experiment típic d'evolució dirigida implica tres passos: Diversificació: El gen que codifica la proteïna d'interès és mutat i/o recombinat a l'atzar per a crear una gran biblioteca de gens variants. Les tècniques usades generalment en aquest pas són les de multiplicació per la Reacció en cadena de la polimerasa (PCR en anglès) amb propensió a errors i barrejat d'ADN (DNA shuffling en anglès). L'univers és la totalitat del continu espaitemps en què es troba la humanitat, juntament amb tota la matèria i energia que conté. A gran escala, és l'objecte d'estudi de la cosmologia, que es basa en la física i l'astronomia, tot i que alguns dels temes d'estudi voregen la metafísica. Actualment, els experts no estan d'acord sobre si és possible (en principi) d'arribar a observar la totalitat de l'univers. Els termes univers conegut, observable o visible, s'utilitzen per a referir-se a la part de l'univers que es pot observar. El terme cosmos és l'univers, especialment quan es considera com un sistema ordenat i harmoniós. De vegades, el terme cosmos es fa servir només per a l'univers observat, mentre que el terme univers es refereix a tot l'existent, s'haja descobert o no. En aquest sentit, 'cosmos' és l'univers conegut o realitat."



def prepareSampleCat(s):
    result = s.lower()

    listOriginal = ["à", "è", "ì", "ò", "ù", "ü", "ï", "á", "é", "í", "ó", "ú", "/", "(", ")", ":", ".", ",", "-", "·",'’','\'']
    listResulted = ["a", "e", "i", "o", "u", "u", "i", "a", "e", "i", "o", "u", "", "", "", "", "", "", "", "","",""]
    for i in range(len(listOriginal)):
        result = result.replace(listOriginal[i], listResulted[i])

    return result



def prepareSampleEn(s):
    result = s.lower()

    listOriginal = ["/", "(", ")", ":", ".", ",", "-", "·"]
    listResulted = ["", "", "", "", "", "", "", ""]
    for i in range(len(listOriginal)):
        result.replace(listOriginal[i], listResulted[i])

    return result


def isVowel(a):
    return a in ['a', 'e', 'i', 'o', 'u']


def isConstant(a):
    return not isVowel(a)


def checkVowels(vector, numVowels):
    c = 0
    num = 0
    try:
        while c < len(vector):
            if vector[c].isalpha():
                if isVowel(vector[c]) == False:
                    return False
            else:
                return False
            c = c + 1
    except IndexError:
        return False
    return True
def getMax(vector,indexFeature):
    return float(max(vector[:][indexFeature]))
def normalize(vector):
    col = len(vector[0])
    maxValues = [getMax(vector,i) for i in range(13)]
    maxValues.append(1)
    for i in range(len(vector)):
        for j in range(col):
            vector[i][j] = vector[i][j]/maxValues[j]

def getFeatures(vector, lang):
    features = []
    # get desided feature from i word
    for word in vector:

        nVowels = [0, 0, 0]
        nConsonants = [0, 0, 0]
        #Num. of coincidences of a,e,i,o,u stored in this order
        vowelsCount = [word.count('a'),word.count('e'),word.count('i')]
        vowelsCount = vowelsCount + [word.count('o'),word.count('u')]
        nCharacters = len(word)
        startWordVowel = 0

        if isVowel(word[0]):
            startWordVowel = 1

        c = 0
        # calculate Vowels and Consonants together and store values
        # in array of numbers. nConsonants[0] is the number of consonants
        # alone. nConsonants[1] the coincidence of two consonants, etc
        vowelVector = ''.join([str(int(isVowel(i))) for i in word])
        consonantVecor = ''.join([str(int(isConstant(i))) for i in word])
        nVowels = [vowelVector.count("1"), vowelVector.count("11"), vowelVector.count("111")]
        nConsonants = [consonantVecor.count("1"), consonantVecor.count("11"), consonantVecor.count("111")]

        row = [nCharacters, startWordVowel, nVowels[0], nVowels[1], nVowels[2], nConsonants[0], nConsonants[1],
               nConsonants[2]]
        row = row + vowelsCount + [lang]
        features.append(row)
    return features

#List of features:
#row = [nCharacters, startWordVowel, nVowels[0], nVowels[1], nVowels[2], nConsonants[0], nConsonants[1],
#               nConsonants[2], lang]
def getAllFeatures():
    features = getFeatures(prepareSampleCat(catala).split(), 0)
    features += getFeatures(prepareSampleEn(english).split(), 1)
    normalize(features)
    return features

#suposa tamany maxim paraula de 20
def featureVector(word):
    featureV = [0]*20

    for position in range(len(word)):
        #97 is the ascii number "a"
        featureV[position] = ord(word[position])-96
    return featureV
def prepareVector(text):
    textFiltered = prepareSampleCat(text)
    #get max value of all vector feature words of text
    maxValue = max([max(featureVector(word)) for word in textFiltered.split()])*1.0
    vectorOfText = []
    for word in textFiltered.split():
        normalizedVector = [x / maxValue for x in featureVector(word)]
        print "Paraula ",word
        print "Sense normalitzar ",featureVector(word)
        print "Normalitzacio ", normalizedVector
        vectorOfText.append(normalizedVector)
    return vectorOfText


c = prepareSampleCat(open("paraulescatala.txt").read()).split()
def getRandomWords(num,listWords):
    newList = []
    for i in range(num):
        number = random.randint(0,len(listWords)-1)
        newList.append(listWords[number])
        listWords.pop(number)
    return newList



#########################
## eXEMPLES VECTOR
prepareVector(prepareSampleCat("recobreix"))
prepareVector(prepareSampleCat("desviï"))
prepareVector(prepareSampleCat("abat"))
prepareVector(prepareSampleCat("estiressim"))
prepareVector(prepareSampleCat("mare"))

#prepareVector("En biologia, l’evolució és el procés de canvi en els trets heretats d’una població d’organismes entre una generació i la següent")
