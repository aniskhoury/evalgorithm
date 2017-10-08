import logging
import random
from structure.configFramework import *


def listToStr(self, l):
    return ''.join(str(element) for element in l)
class Instruction:
    code = None
    cursor = 0
    maxLenghtBits = 32
    skeleton = [int(i) for i  in "00100000000000000000000000000000"]
    def __init__(self,code = None,evaconfig=None,maxLenghtBits=32):
        #TODO: Inicialitzar la instruccio amb un codi raonablement
        #proper millora molt temps cerca. Millorar aixo del Evaconfig
        if self.skeleton==None:
            self.generateRandomCode(bits=maxLenghtBits)
        else:
            self.setCode(self.skeleton)
            if code != None:
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
        num = int(self.readNextBits(26),2)
        self.resetCursor()
        if sign == 0:
            return num*-1
        return str(num)
    def toASMArgTxt(self):
        return str(int(self.readNextBits(27),2))

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
        if cmd == "01000":
            text = "MEMadd "
        elif cmd == "01001":
            text = "MEMsub "
        elif cmd == "01010":
            text = "MEMmul "
        elif cmd == "01011":
            text = "MEMdiv "

        elif cmd == "01111":
            text = "PUSH " + str(int(self.readNextBits(5),2)) +" "+ str(int(self.readNextBits(23),2))

            def toASMArgTxt(self):
                return str(int(self.readNextBits(27), 2))
        if text != "":
            return text + self.toASMArgTxt()
        return "Unknown instruction"
    def generateCode(self,s):
        data = s.split()
        if len(data)> 1:
            cmd = data[0]
            code = list()
            try:
                code = code + list(map(int,cmd))
            except ValueError:
                if cmd == "ADDi":
                    code = list()
                    code = code + list("00000") + list(str(self.getBinNum(data[1],padding=6)))
                    self.setCode(code)
                if cmd == "SUBi":
                    code = code + list("00001") + list(str(self.getBinNum(data[1],padding=6)))
                    self.setCode(code)
                if cmd == "MULi":
                    code = code + list("00010") + list(str(self.getBinNum(data[1],padding=6)))
                    self.setCode(code)
                if cmd == "DIVi":
                    code = code + list("00011") + list(str(self.getBinNum(data[1],padding=6)))
                    self.setCode(code)
                if cmd == "ADDarg":
                    code = code + list("00100") + list(str(self.getBinNumArgs(data[1])))
                    self.setCode(code)
                if cmd == "SUBarg":
                    code = code + list("00101") + list(str(self.getBinNumArgs(data[1])))
                    self.setCode(code)
                if cmd == "MULarg":
                    code = code + list("00110") + list(str(self.getBinNum(data[1])))
                    self.setCode(code)
                if cmd == "DIVarg":
                    code = code + list("00111") + list(str(self.getBinNumArgs(data[1])))
                    self.setCode(code)
                if cmd == "MEMadd":
                    code = code + list("01000") + list(str(self.getBinNumArgs(data[1])))
                    self.setCode(code)
                if cmd == "MEMsub":
                    code = code + list("01001") + list(str(self.getBinNumArgs(data[1])))
                    self.setCode(code)
                if cmd == "MEMmul":
                    code = code + list("01010") + list(str(self.getBinNumArgs(data[1])))
                    self.setCode(code)
                if cmd == "MEMdiv":
                    code = code + list("01011") + list(str(self.getBinNumArgs(data[1])))
                    self.setCode(list(map(int,code)))
                if cmd == "PUSH":
                    code = code + list("01111") + list(str(self.getBinNumArgs(data[1],padding=27))) + list(str(self.getBinNumArgs(data[1],padding=10)))
                    self.setCode(code)

    def resetCursor(self):
        self.cursor = 0
    def generateRandomCode(self,bits=32):
        result = []
        for i in range(bits):
            result.append(random.randint(0,1))
        self.setCode(result)

    def setCode(self,c):
        #random code
        self.code = c
    #def readNextBits(self,numBits=1):
    #    cursor = self.getCursor()
    #    end = cursor + numBits
    #    if end <= len(self.getCode()):
    #        self.setCursor(end)
    #        return str(self.getCode()[cursor:end])
    #    logging.error("Invalid readNextBits() in instruction.py, cursor=%s numBits=%s, code=%s",cursor,numBits,self.getCode())
    #    return ""
    def readNextBits(self,numBits=1):
        cursor = self.getCursor()
        end = cursor + numBits
        self.setCursor(end)
        res = self.getCode()[cursor:end]
        res = ''.join([str(i) for i in res])
        return res

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
