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
            text = "PUSH "+ str(int(self.readNextBits(14),2))+" "+ str(int(self.readNextBits(13),2))

        elif cmd == "10000":
            text = "XORmem " + str(int(self.readNextBits(9),2))+" "
            text = text +" "+ str(int(self.readNextBits(9),2)) +","+ str(int(self.readNextBits(9),2))
        elif cmd == "10001":
            dest = str(int(self.readNextBits(9),2))
            m1 = str(int(self.readNextBits(9),2))
            m2 = str(int(self.readNextBits(9),2))
            text = "ANDmem " + dest+" "+ m1 +","+ m2
        elif cmd == "10010":
            text = "NOTmem " + str(int(self.readNextBits(9),2))+" "
            text = text +" "+ str(int(self.readNextBits(9),2)) +","+ str(int(self.readNextBits(9),2))
        elif cmd == "10011":
            dest = str(int(self.readNextBits(9),2))
            m1 = str(int(self.readNextBits(9),2))
            m2 = str(int(self.readNextBits(9),2))
            text = "ORmem " + dest+" "+ m1 + ","+m2
        elif cmd == "10100":
            dest = str(int(self.readNextBits(18),2))
            arg = str(int(self.readNextBits(9),2))
            text = "PUTmemarg "+dest+ ","+arg
        if text != "":
            return text
        return "Unknown instruction"

    def toASMArgTxt(self):
        return str(int(self.readNextBits(27), 2))
    def paddLen(self,s,tamany):
        c = tamany-len(s)
        result = s
        n = 0
        while n < c:
            result = "0"+result
            n = n +1
        return result
    def getBinLogicOper2(self,dest, mem1, mem2):
        res = str(bin(int(dest))[2:])
        res1 = str(bin(int(mem1))[2:])
        res2 = str(bin(int(mem2))[2:])

        return self.paddLen(res,9)+self.paddLen(res1,9)+self.paddLen(res2,9)
    def getBinLogicOper1(self,dest, mem1):
        res = str(bin(int(dest))[2:])
        res1 = str(bin(int(mem1))[2:])
        return self.paddLen(res,9)+self.paddLen(res1,9)


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
                    dest = str(bin(int(data[1]))[2:])
                    num = str(bin(int(data[2]))[2:])
                    c = len(dest)
                    while c < 14:
                        dest = "0"+dest
                        c = c+1
                    c = len(num)
                    while c < 13:
                        num = "0"+num
                        c = c+1
                    code = code + list("01111")+list(dest)+list(num)
                    self.setCode(list(map(int,code)))

                if cmd == "XORmem":
                    code = code + list("10000") +list(self.getBinLogicOper2(data[1],data[2],data[3]))
                    self.setCode(code)
                if cmd == "ANDmem":
                    code = code + list("10001") +list(self.getBinLogicOper2(data[1],data[2],data[3]))
                    self.setCode(code)
                if cmd == "NOTmem":
                    code = code + list("10010") + list(self.getBinLogicOper1(data[1],data[2]))
                    self.setCode(code)
                if cmd == "ORmem":
                    c = list(self.getBinLogicOper2(data[1],data[2],data[3]))
                    code = code + list("10011") +c
                    self.setCode(code)
                if cmd == "PUTmemarg":
                    dest = str(bin(int(data[1]))[2:])
                    arg = str(bin(int(data[2]))[2:])
                    c = len(dest)
                    while c < 18:
                        dest = "0"+dest
                        c = c+1
                    c = len(arg)
                    while c < 9:
                        arg = "0"+arg
                        c = c+1
                    code = code + list("10100")+list(dest)+list(arg)
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
            #logging.error("Bad cursor value %s and code %s",c,self.getCode())
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
