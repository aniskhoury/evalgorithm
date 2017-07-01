from icode import *
from instruction import *
import random
import math
class Algorithm:
    instructions = list()
    result = 0.0
    output = ""
    arguments = []
    outputExpected = ""
    probMutation = 2
    indexArgument = 0
    def __init__(self, instructions,arguments,outputExpected):
        self.setInstructions(instructions)
        self.setArguments(arguments)
        self.setResult(0.0)
        self.setOutput("")

        self.setOutputExpected(outputExpected)
    def compute(self,indexArgument):
        self.setResult((0.0))
        self.setOutput("")

        for i in self.getInstructions():
            i.setCursor(0)
            if self.computeInstruction(i,indexArgument) == False:
                return False
        return True
    def getOutput(self):
        return self.output
    def getOutputExpected(self):
        return self.outputExpected
    def getInstructions(self):
        return self.instructions
    def getArgumentPos(self,i,indexArgument):
        try:
            return self.getArguments()[indexArgument][i]
        except IndexError:
            return None
    def getResult(self):
        return self.result
    def getArguments(self):
        return self.arguments
    def setOutput(self,i):
        self.output = i
    def setInstructions(self, i):
        self.instructions = i
    def setArguments(self,i):
        self.arguments = i
    def setOutputExpected(self,i):
        self.outputExpected = i
    def setResult(self, r):
        self.result = r
    def addInstruction(self,I):
        self.instructions.append(I)

    def arithmeticNum(self,i,indexArgument):
        type = i.readNextBytes(2)
        sign = i.readNextBytes(1)
        try:
            number = int(i.readNextBytes(8), 2)
        except ValueError:
            return False, False, False, False
        if type == "00":
            if sign == str("1"):
                number = number * -1
        if type == "01":
            if  len(self.getArguments()[indexArgument])-1>= number and number >=0:
                number = self.getArguments()[indexArgument][number]
            else:
                return False, False, False, False
            if number == None:
                return False, False, False, False
        return i,type,sign,number



    def crossCode(self,i):
        codeReturned = str(i)
        if random.randint(1,100) <= self.probMutation:
            mutation = random.randint(1,3)
            #ADD mutation
            if mutation == 1:
                codeReturned = codeReturned+str(random.randint(0,1))
            #REMOVE mutation
            if mutation == 2:
                codeReturned = codeReturned[:len(codeReturned)-1]
            if mutation == 3:
                codeReturned = list(codeReturned)
                if codeReturned[len(codeReturned)-1] == '0':
                    codeReturned[len(codeReturned) - 1] = '1'
                else:
                    codeReturned[len(codeReturned) - 1] = '0'
                codeReturned = "".join(codeReturned)
        return codeReturned


    def cross(self,algorithmB,type=0):
        child = Algorithm([],self.getArguments(),self.getOutputExpected())
        if len(self.getInstructions()) >= len(algorithmB.getInstructions()):
            a = self
            b = algorithmB
        else:
            b = self
            a = algorithmB
        for i in range(len(b.getInstructions())):

            if random.randint(1,1000) == 1:
                child.addInstruction(Instruction("00000000000000000",randomCode=True))
            #type cross: half code A, half code B, in this order.
            if type==0:
                nextCodeInstructionChild = ""
                codeA = a.getInstructions()[i].getCode()
                codeB = b.getInstructions()[i].getCode()
                for i in codeA[:int(len(codeA) / 2)]:
                    nextCodeInstructionChild = nextCodeInstructionChild + str(self.crossCode(i))
                for i in codeB[:int(len(codeB) / 2)]:
                    nextCodeInstructionChild = nextCodeInstructionChild + str(self.crossCode(i))
                child.addInstruction(Instruction(nextCodeInstructionChild))
        return child
    def fitness(self):
        n = 0.0
        for i in range(len(self.getArguments())):
            self.compute(i)
            diffError = math.sqrt(math.pow((float(self.getResult())-float(self.getOutputExpected()[i])),2))*1/(len(self.getArguments()))
            n = n + diffError
        return math.sqrt(n)
    def readTypeSignNum(self,i,indexArgument):
        i, type, sign, number = self.arithmeticNum(i, indexArgument)
        if i == False:
            return False,False,False
        return i,type,sign,number
    def computeInstruction(self,i,indexArgument):
        t = self.getResult()
        cmd = i.readNextBytes(3)
        #print
        #00->char
        #01->result
        #10->var

        if cmd == "100":
            type = i.readNextBytes(2)
            if type == "00":
                try:
                    c = int(i.readNextBytes(8), 2)
                    self.output = self.output + chr(c)
                except ValueError:
                    return False
            if type == "01":
                self.output = self.output + str(self.result)
        i, type, sign, number = self.arithmeticNum(i, indexArgument)
        if i == False:
            return False
        #ADD
        if cmd == "000":
            t = t+number
        #SUB
        if cmd == "001":
            t = t-number
        #MUL
        if cmd == "010":
            t = t * number
        #DIV
        if cmd == "011":
            if number != 0:
                t = t/number
            else:
                return False
        self.setResult(t)

        return True

