import logging
import random
class Instruction:
    code = None
    cursor = None
    def __init__(self,code = None):
        self.setCode(code)
        logging.info("Codi",self.getCode())
        if code != None:
            self.setCursor(0)
    def generateRandomCode(self,bits=None):
        numBits = bits
        result = ""
        if numBits == None:
            global numBitsInstruction
            numBits = numBitsInstruction
        for c in range(numBits):
            result = result + str(random.randint(0,1))
        self.setCode(result)
    def setCode(self,c):
        #random code
        if c == None:
            self.generateRandomCode()
        else:
            self.code = c
    def readNextBits(self,numBits=1):
        cursor = self.getCursor()

        if self.getCode() == None:
            logging.error("No code in readNextBits(self,numBits=1) ")
            return False
        end = cursor + numBits
        if end <= len(self.getCode()):
            self.setCursor(end)
            return self.getCode()[cursor:end]
        logging.error("Invalid readNextBits() in instruction.py, cursor=%s numBits=%s, code=%s",cursor,numBits,self.getCode())
        exit()
    def validInstruction(self):
        return True
    def setCursor(self,c):
        if c < 0 or c >= len(self.getCode()):
            logging.error("Bad cursor value %s and code %s",c,self.getCode())
            return False
        self.cursor = c
        return True
    def getCode(self):
        return self.code
    def getCursor(self):
        return self.cursor
    def showInfo(self):
        saveCursor = self.getCursor()
        self.setCursor(0)
        self.setCursor(saveCursor)

#example uses
# i = Instruction(code="0000111100010101")
# print(i.readNextBits(5))
# print(i.readNextBits(5))
# print(i.readNextBits(5))
# print(i.readNextBits(5))
# print(i.readNextBits(5))

