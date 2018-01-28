#!/usr/bin/env python

import itertools
import random
import string

english = "Directed evolution is a method used in protein engineering that mimics the process of natural selection to evolve proteins or nucleic acids toward a user-defined goal. It consists of subjecting a gene to iterative rounds of mutagenesis (creating a library of variants), selection (expressing the variants and isolating members with the desired function), and amplification (generating a template for the next round). It can be performed in vivo (in living cells), or in vitro (free in solution or microdroplet). Directed evolution is used both for protein engineering as an alternative to rationally designing modified proteins, as well as studies of fundamental evolutionary principles in a controlled, laboratory environment. Combined, 'semi-rational' approaches are being investigated to address the limitations of both rational design and directed evolution. Beneficial mutations are rare, so large numbers of random mutants have to be screened to find improved variants. 'Focussed libraries' concentrate on randomising regions thought to be richer in beneficial mutations for the mutagenesis step of DE. A focussed library contains fewer variants than a traditional random mutagenesis library and so does not require such high-throughput screening. These gas-like ions rapidly interact with ions of opposite charge to give neutral molecules or ionic salts. Ions are also produced in the liquid or solid state when salts interact with solvents (for example, water) to produce solvated ions, which are more stable, for reasons involving a combination of energy and entropy changes as the ions move away from each other to interact with the liquid. These stabilized species are more commonly found in the environment at low temperatures. A common example is the ions present in seawater, which are derived from the dissolved salts."


catala = "L'evolució dirigida és un mètode utilitzat en l'enginyeria de proteïnes per aprofitar el poder de la selecció natural i obtenir proteïnes o ARN amb les propietats desitjades que no es troben a la natura- Un experiment típic d'evolució dirigida implica tres passos: Diversificació: El gen que codifica la proteïna d'interès és mutat i/o recombinat a l'atzar per a crear una gran biblioteca de gens variants. Les tècniques usades generalment en aquest pas són les de multiplicació per la Reacció en cadena de la polimerasa (PCR en anglès) amb propensió a errors i barrejat d'ADN (DNA shuffling en anglès). L'univers és la totalitat del continu espaitemps en què es troba la humanitat, juntament amb tota la matèria i energia que conté. A gran escala, és l'objecte d'estudi de la cosmologia, que es basa en la física i l'astronomia, tot i que alguns dels temes d'estudi voregen la metafísica. Actualment, els experts no estan d'acord sobre si és possible (en principi) d'arribar a observar la totalitat de l'univers. Els termes univers conegut, observable o visible, s'utilitzen per a referir-se a la part de l'univers que es pot observar. El terme cosmos és l'univers, especialment quan es considera com un sistema ordenat i harmoniós. De vegades, el terme cosmos es fa servir només per a l'univers observat, mentre que el terme univers es refereix a tot l'existent, s'haja descobert o no. En aquest sentit, 'cosmos' és l'univers conegut o realitat."



diccionariCatala = open("paraulescatala.txt").read()
diccionariCastella = open("paraulescastella.txt").read()
diccionariAngles = open("english.txt").read()





grafemes = string.ascii_lowercase+"çñ'-·àáèéìíòóùúäëïöü".decode('utf-8')
vowelList = "aeiouáéíóúàèìòùäëïöü".decode('utf-8')
punctuationList = "'·".decode('utf-8')
def filterText(text,grafemes):
    filteredText = text.decode('utf-8')
    filteredText = filteredText.lower()
    result = ""
    for grafema in filteredText:
        if grafema in grafemes:
            result = result + grafema
    return result
def isVowel(c,vowelList):
    if c in vowelList:
        return True
    return False
def isPunctuation(c,punctuationList):
    if c in punctuationList:
        return True
    return False
def isConsonant(c,vowelList,punctuationList):
    if isVowel(c,vowelList):
        return False
    if isPunctuation(c,punctuationList):
        return False
    return True

def freqGrafema(word,grafemesList):
    freq = {}
    #inicialitzo la llista de freq. grafemes a 0
    for grafema in grafemesList:
        freq[grafema] = 0
    #es conten
    for grafema in word:
        freq[grafema] = freq[grafema]+1
        print("grafema : ",grafema)

    vectorFreq = []
    for grafema in grafemesList:
        vectorFreq.append(freq[grafema])
    return vectorFreq
def numVowels(word,vowelList):
    c = 0
    for grafema in word:
        c = c + isVowel(grafema,vowelList)
    return c
def numConsonants(word,vowelList,punctuationList):
    c = 0
    for grafema in word:
        c = c + isConsonant(grafema,vowelList,punctuationList)
    return c
def numPunctuations(word,punctuationList):
    c = 0
    for grafema in word:
        c = c + isPunctuation(grafema,punctuationList)
    return c
def generateVectorFeatureWord(word,vowelList,punctuationList,grafemes):
    vectorFeature = freqGrafema(word,grafemes)
    #add freq vowels feature
    vectorFeature.append(numVowels(word,vowelList))
    #add freq consonants feature
    vectorFeature.append(numConsonants(word,vowelList,punctuationList))
    # add freq punctation feature
    vectorFeature.append(numPunctuations(word, punctuationList))
    #add lenght word feature
    vectorFeature.append(len(word))
    return vectorFeature
def normalizeVectorFeature(vectorF):
    maxFeature = max(vectorF)*1.0
    normalizedVector = [vectorF[nFeature]/maxFeature for nFeature in range(len(vectorF)) ]
    return normalizedVector
paraula = "l'Anïs"
paraula = filterText(paraula,grafemes)
vectorF = generateVectorFeatureWord(paraula,vowelList,punctuationList,grafemes)

def generateAllVectorFeature(text,vowelList,punctuationList,grafemes):
    vectorFeatures = []
    words = text.split()
    for word in words:
        wordClean = filterText(word,grafemes)
        if wordClean != "":
            vectorF = generateVectorFeatureWord(wordClean, vowelList, punctuationList, grafemes)
            vectorFNormalied = normalizeVectorFeature(vectorF)
            vectorFeatures.append(vectorFNormalied)
    return vectorFeatures
text = "hola que tAl"
print(generateAllVectorFeature(text,vowelList,punctuationList,grafemes))
exit()