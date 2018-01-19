import logging
class VirtualMachine:
    global debug
    memory = None
    algorithm = None
    pc = -1 #program counter
    result = 0
    output = ""
    codeFunction = {}
    lenghtMemory = 64
    numBitsCodeFunction = 5
    def loadFunctions(self):

        self.codeFunction["00000"] = self.addInmFunction
        self.codeFunction["00001"] = self.subInmFunction
        self.codeFunction["00010"] = self.mulInmFunction
        self.codeFunction["00011"] = self.divInmFunction
        self.codeFunction["00100"] = self.addArgFunction
        self.codeFunction["00101"] = self.subArgFunction
        self.codeFunction["00110"] = self.mulArgFunction
        self.codeFunction["00111"] = self.divArgFunction
        self.codeFunction["01000"] = self.addMemFunction
        self.codeFunction["01001"] = self.subMemFunction
        self.codeFunction["01010"] = self.mulMemFunction
        self.codeFunction["01011"] = self.divMemFunction
        self.codeFunction["01111"] = self.pushMemFunction
        self.codeFunction["10000"] = self.xorMemFunction
        self.codeFunction["10001"] = self.andMemFunction
        self.codeFunction["10010"] = self.notMemFunction
        self.codeFunction["10011"] = self.orMemFunction
        self.codeFunction["10100"] = self.putMemArg
        self.codeFunction["10111"] = self.putMemResult



    def __init__(self,memory=64,algorithm = None,pc = None):

        self.loadFunctions()
        #by default allocate 1024*(32bits)
        #initialized by 0
        if memory == None:
            self.setMemory(list())
        else:
            self.setMemory([0]*memory)
            self.lenghtMemory = memory
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
            if self.computeInstruction(instruction,input) == False:
                return False
            instruction = self.getNextInstruction()

        return True
    def computeInstruction(self,instruction,input):
        instruction.resetCursor()
        code = instruction.readNextBits(self.numBitsCodeFunction)
        #check code of instruction and compute it
        #store result of compute instruction in ret
        ret = False
        if self.codeFunction.__contains__(code):
            ret = self.codeFunction[code](instruction,input)

        return ret

    def loadAlgorithm(self,a):
        self.algorithm = a
        self.setPc(-1)

    #getters & setters
    ########################################
    def getAlgorithm(self):
        return self.algorithm
    def resetRun(self):
        self.setPc(-1)
        self.setResult(0)
        self.setMemory([0] * self.lenghtMemory)
    #By default, the start is -1
    #first increase the PC, then read the instruction
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
    ########################################
    #Utilities for VirtualMachine
    def resetTest(self):
        self.setOutput("")
    def binToDec(self,s):
        return int(s,2)*1.0
    def decToBin(self,s):
        return bin(s)[2:]
    #Read the common part of instructions#
    ########################################
    def readArgumentsInm(self,instruction,input):
        num = int(self.binToDec(instruction.readNextBits(27)))
        if num < len(input):
            return input[num]
        else:
            return False

    def readInmediateInmArgs(self,instruction,input):
        #32 bits - 5 code = 27 bits
        number = instruction.readNextBits(27)
        number = int(self.binToDec(number))
        return number

    def readMemValues(self,instruction):
        memDest = int(instruction.readNextBits(9),2)
        memGate1 = int(instruction.readNextBits(9),2)
        memGate2 = int(instruction.readNextBits(9),2)

        return memDest,memGate1,memGate2
    def logicGate2Input(self,instruction):
        memDest = int(instruction.readNextBits(9),2)
        memGate1 = int(instruction.readNextBits(9),2)
        memGate2 = int(instruction.readNextBits(9),2)

        return memDest,memGate1,memGate2

    def logicGate1Input(self, instruction):
        memDest = int(instruction.readNextBits(9),2)
        memGate1 = int(instruction.readNextBits(18),2)

        return memDest, memGate1


    ########################################


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
        try:
            n = input[num]
            if n == 0:
                return False
        except IndexError:
            return False
        except TypeError:
            return False
        self.setResult(res/num)
        return True

    def divMemFunction(self, instruction, input):
        dest,mem1,mem2 = self.readMemValues(instruction)
        try:
            self.memory[dest] = self.memory[mem1] / self.memory[mem2]
        except (IndexError, ZeroDivisionError) as e:
            return False

        return True



    def mulMemFunction(self,instruction,input):
        dest,mem1,mem2 = self.readMemValues(instruction)
        try:
            self.memory[dest] = self.memory[mem1] * self.memory[mem2]
        except IndexError:
            return False
        return True


    def subMemFunction(self,instruction,input):
        dest,mem1,mem2 = self.readMemValues(instruction)
        try:
            self.memory[dest] = self.memory[mem1] - self.memory[mem2]
        except IndexError:
            return False
        return True


    def addMemFunction(self,instruction, input):
        dest,mem1,mem2 = self.readMemValues(instruction)
        try:
            self.memory[dest] = self.memory[mem1] + self.memory[mem2]
        except IndexError:
            return False
        return True

    def pushMemFunction(self,instruction, input):
        addr = int(instruction.readNextBits(14),2)
        num = int(instruction.readNextBits(13),2)
        try:
            self.memory[addr] = num
        except IndexError:
            return False
        return True

    def andMemFunction(self,instruction,input):
        dest,mem1,mem2 = self.logicGate2Input(instruction)
        try:
            self.memory[dest] = self.memory[mem1] & self.memory[mem2]
        except IndexError:
            return False
        return True
    def xorMemFunction(self,instruction,input):
        dest,mem1,mem2 = self.logicGate2Input(instruction)
        try:
            self.memory[dest] = self.memory[mem1] ^ self.memory[mem2]
        except IndexError:
            return False
        return True

    def orMemFunction(self,instruction,input):
        dest,mem1,mem2 = self.logicGate2Input(instruction)
        try:
            self.memory[dest] = self.memory[mem1] | self.memory[mem2]
        except IndexError:
            return False
        return True
    def notMemFunction(self,instruction,input):
        dest,mem1 = self.logicGate1Input(instruction)
        try:
            bits = bin(self.memory[mem1])[2:]
            c = ""
            #loop for negation. ~ with integer numbers in python
            #can produce negative numbers
            for i in str(bits):
                if i == "0":
                    c = "1"
                else:
                    c = "0"
            self.memory[dest] = int(c,2)
        except IndexError:
            return False
        return True
    def putMemArg(self,instruction,input):
        try:
            dest = int(instruction.readNextBits(18),2)
            arg = int(instruction.readNextBits(9),2)
            self.memory[dest] = input[arg]

        except IndexError:
            return False
        return True
    def putMemResult(self,instruction,input):
        try:
            dest = int(self.binToDec(instruction.readNextBits(27)))
            self.memory[dest] = self.result

        except IndexError:
            return False
        return True