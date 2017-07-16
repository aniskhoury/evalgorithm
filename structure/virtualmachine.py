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
        self.codeFunction["00100"] = self.addArgFunction
        self.codeFunction["00101"] = self.subArgFunction
        self.codeFunction["00110"] = self.mulArgFunction
        self.codeFunction["00111"] = self.divArgFunction

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
        self.resetTest()
        self.setPc(-1)
        pc = self.getPc()
        #load and process all instructions of algorithm
        instruction = self.getNextInstruction()
        while instruction != False:
            #instruction.showInfo()
            #instruction.showInfo()
            if self.computeInstruction(instruction,input) == False:
                return False
            instruction = self.getNextInstruction()

        return True
    def computeInstruction(self,instruction,input):
        numBitsCode = 5
        instruction.resetCursor()
        code = instruction.readNextBits(numBitsCode)
        #check code of instruction and compute it
        #store result of compute instruction in ret
        ret = False
        if self.codeFunction.__contains__(code):
            ret = self.codeFunction[code](instruction,input)
        return ret

    def loadAlgorithm(self,a):
        self.algorithm = a
        self.setPc(-1)
    def getAlgorithm(self):
        return self.algorithm
    def resetRun(self):
        self.setPc(-1)
        self.setResult(0)
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
    def readArgumentsInm(self,instruction,input):
        num = int(self.binToDec(instruction.readNextBits(27)))
        if num < len(input):
            return input[num]
        else:
            return False
    def readInmediateInmArgs(self,instruction,input):
        #32 bits - 5 code - 27
        instruction.showInfo()
        number = instruction.readNextBits(27)
        number = int(self.binToDec(number))
        return number
    def addInmFunction(self,instruction,input):
        res = self.getResult()
        number = self.readInmediateInmArgs(instruction,input)
        self.setResult(res+number)
        return True
    def subInmFunction(self,instruction,input):
        res = self.getResult()
        number = self.readInmediateInmArgs(instruction,input)
        self.setResult(res-number)
        return True
    def mulInmFunction(self,instruction,input):
        res = self.getResult()
        number = self.readInmediateInmArgs(instruction,input)
        self.setResult(res*number)
        return True
    def divInmFunction(self,instruction,input):
        res = self.getResult()
        number = self.readInmediateInmArgs(instruction,input)
        if number == 0:
            return False
        self.setResult(res / number)
        return True

    def addArgFunction(self,instruction,input):
        res = self.getResult()
        num = self.readArgumentsInm(instruction,input)

        if num == False:
            return False

        self.setResult(res+num)

        return True
    def subArgFunction(self,instruction,input):
        res = self.getResult()
        num = self.readArgumentsInm(instruction,input)
        if num == False:
            return False
        self.setResult(res-num)
        return True
    def mulArgFunction(self,instruction,input):
        res = self.getResult()
        num = self.readArgumentsInm(instruction,input)
        if num == False:
            return False
        self.setResult(res*num)
        return True
    def divArgFunction(self,instruction,input):
        res = self.getResult()
        num = self.readArgumentsInm(instruction,input)
        if num == False:
            return False
        if input[num] == 0:
            return False
        self.setResult(res/num)
        return True