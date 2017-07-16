import logging
import random
class Instruction:
    code = None
    cursor = 0
    maxLenghtBits = 32

    def __init__(self,code = None,evaconfig=None,maxLenghtBits=32):
        code = "00100000000000000000000000000000"
        if code==None:
            if evaconfig != None:
                self.generateRandomCode(evaconfig.getNumBitsInstruction())
            else:
                self.generateRandomCode(maxLenghtBits)
        else:
            self.setCode(code)
        #logging.info("Codi",self.getCode())
        if code != None:
            self.setCursor(0)
    def toBin(self,s,paddingBin=0):
        c = str(bin(s)[2:])
        res = ""
        for i in range(self.maxLenghtBits-paddingBin-len(c)):
            res = res + "0"
        return res+c
    def getBinNum(self,s,padding=0):
        if s.isdigit():
            num = int(s)
            if num < 0:
                return "0"+self.toBin(num*-1,paddingBin=padding)
            else:
                return "1"+self.toBin(num,paddingBin=padding)
        else:
            print("Error: no number found")
            exit(-1)
    def getBinNumArgs(self,s,padding=5):
        if s.isdigit():
            num = int(s)
            return self.toBin(num,paddingBin=padding)
        else:
            print("Error: no number found")
            exit(-1)
    def toASMInmediateTxt(self):
        sign = self.readNextBits()
        num = int(self.readNextBits(26))
        self.resetCursor()
        if sign == 0:
            return int(num)*-1
        return str(num)
    def toASMArgTxt(self):
        return str(int(self.readNextBits(27)))
    def toASM(self):
        self.resetCursor()
        bitsCMD = 5
        cmd = self.readNextBits(bitsCMD)
        text = ""

        if cmd == "00000":
            text = "ADDi " +self.toASMInmediateTxt()
        elif cmd == "00001":
            text = "SUBi " + self.toASMInmediateTxt()
        elif cmd == "00010":
            text = "MULi " + self.toASMInmediateTxt()
        elif cmd == "00011":
            text = "DIVi " + self.toASMInmediateTxt()
        if text != "":
            return text
        if cmd == "00100":
            text = "ADDarg "
        elif cmd == "00101":
            text = "SUBarg "
        elif cmd == "00110":
            text = "MULarg "
        elif cmd == "00111":
            text = "DIVarg "

        if text != "":
            return text + self.toASMArgTxt()
        return "Unknown instruction"
    def generateCode(self,s):
        data = s.split()
        if len(data)> 1:
            cmd = data[0]
            code = str(cmd)
            if cmd == "ADDi":
                code = "00000" + str(self.getBinNum(data[1],padding=6))
                self.setCode(code)
            if cmd == "SUBi":
                code = "00001" + str(self.getBinNum(data[1],padding=6))
                self.setCode(code)
            if cmd == "MULi":
                code = "00010" + str(self.getBinNum(data[1],padding=6))
                self.setCode(code)
            if cmd == "DIVi":
                code = "00011" + str(self.getBinNum(data[1],padding=6))
                self.setCode(code)
            if cmd == "ADDarg":
                code = "00100" + str(self.getBinNumArgs(data[1]))
                self.setCode(code)
            if cmd == "SUBarg":
                code = "00101" + str(self.getBinNumArgs(data[1]))
                self.setCode(code)
            if cmd == "MULarg":
                code = "00110" + str(self.getBinNum(data[1]))
                self.setCode(code)
            if cmd == "DIVarg":
                code = "00111" + str(self.getBinNumArgs(data[1]))
                self.setCode(code)
    def resetCursor(self):
        self.cursor = 0
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
        self.code = c
    def readNextBits(self,numBits=1):
        cursor = self.getCursor()

        if self.getCode() == None:
            logging.error("No code in readNextBits(self,numBits=1) ")
            return False
        end = cursor + numBits
        if end <= len(self.getCode()):
            self.setCursor(end)
            return str(self.getCode()[cursor:end])
        logging.error("Invalid readNextBits() in instruction.py, cursor=%s numBits=%s, code=%s",cursor,numBits,self.getCode())
        return ""
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
        #code show info HERE
        print("Code: ",self.getCode())
        self.setCursor(saveCursor)
    def getMaxLenghtBits(self):
        return self.maxLenghtBits
#example uses
# i = Instruction(code="0000111100010101")
# print(i.readNextBits(5))
# print(i.readNextBits(5))
# print(i.readNextBits(5))
# print(i.readNextBits(5))
# print(i.readNextBits(5))
