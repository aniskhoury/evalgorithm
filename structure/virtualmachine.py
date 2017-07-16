import logging
class VirtualMachine:
    global debug
    memory = None
    algorithm = None
    pc = -1 #program counter
    result = 0
    output = ""
    codeFunction = {}

    def loadFunctions(self):

        self.codeFunction["00000"] = self.addInmFunction
        self.codeFunction["00001"] = self.subInmFunction
        self.codeFunction["00010"] = self.mulInmFunction
        self.codeFunction["00011"] = self.divInmFunction

    def __init__(self,memory=1024,algorithm = None,pc = None):

        self.loadFunctions()
        if memory == None:
            self.setMemory(list())
        else:
            self.setMemory([0]*memory)
        if algorithm == None:
            self.setPc(-1)
    def getResult(self):
        return self.result
    def setResult(self,s):
        self.result = s
    def setMemory(self,m):
        self.memory = m
    def getMemory(self):
        return self.memory
    def getNextInstruction(self):
        pc = self.getPc()
        if pc != None:
            pc = pc +1
            if pc > -1 and pc < len(self.getAlgorithm().getInstructions()):
                self.setPc(pc)
                return self.getAlgorithm().getInstructions()[pc]
            return False
        return False

    def runAlgorithm(self,input):
        pc = self.getPc()
        #load and process all instructions of algorithm
        instruction = self.getNextInstruction()
        while instruction != False:
            #instruction.showInfo()
            #instruction.showInfo()
            self.computeInstruction(instruction)
            instruction = self.getNextInstruction()

        return True
    def computeInstruction(self,instruction):
        numBitsCode = 5
        instruction.resetCursor()
        code = instruction.readNextBits(numBitsCode)
        #check code of instruction and compute it
        #store result of compute instruction in ret
        if self.codeFunction.__contains__(code):
            ret = self.codeFunction[code](instruction)

            if ret == False:
                return False
        return True

    def loadAlgorithm(self,a):
        self.algorithm = a
        self.setPc(-1)
    def getAlgorithm(self):
        return self.algorithm
    def setPc(self,pc):
        if self.getAlgorithm() != None:
            if len(self.getAlgorithm().getInstructions()) == 0 or pc == None or pc < 0 or pc >= len(self.getAlgorithm().getInstructions()):
                self.pc = -1
            else:
                self.pc = pc
        else:
            self.pc = -1
    def getPc(self):
        return self.pc

    def setOutput(self,output):
        self.output = output
    def setResult(self,r):
        self.result = r
    def getResult(self):
        return self.result
    def getOutput(self):
        return self.output
    def resetTest(self):
        self.setResult(0)
        self.setOutput("")
    #read the standard sign(1 bit) num (27)
    def binToDec(self,s):
        return int(s,2)*1.0
    def decToBin(self,s):
        return bin(s)[2:]
    def readInmediateInsArgs(self,instruction):
        sign = instruction.readNextBits()
        #32 bits - 5 code - 1 sign = 26 bits number
        number = instruction.readNextBits(26)

        number = self.binToDec(number)*1.0
        if sign == 0:
            number = number *-1
        return number
    def addInmFunction(self,instruction):
        res = self.getResult()
        number = self.readInmediateInsArgs(instruction)
        self.setResult(res+number)
        return True
    def subInmFunction(self,instruction):
        res = self.getResult()
        number = self.readInmediateInsArgs(instruction)
        self.setResult(res-number)
        return True
    def mulInmFunction(self,instruction):
        res = self.getResult()
        number = self.readInmediateInsArgs(instruction)
        self.setResult(res*number)
        return True
    def divInmFunction(self,instruction):
        res = self.getResult()
        number = self.readInmediateInsArgs(instruction)
        if number == 0:
            return False
        self.setResult(res / number)
        return True



