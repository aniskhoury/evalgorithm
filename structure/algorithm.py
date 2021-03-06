from structure.instruction import *
class Algorithm:
    instructions = []
    numInstructionsDefault = 3
    def __init__(self,instructions=None):
        if instructions != None:
            if instructions == "empty":
                self.setInstructions([])
            else:
                self.setInstructions(instructions)
        else:
            self.setInstructions([])
            #number of instructions per default
            self.generateRandomAlgorithm(self.numInstructionsDefault)

    def setInstructions(self,i):
        self.instructions = i

    def generateRandomAlgorithm(self,numInstructions):
        for i in range(numInstructions):
            self.instructions.append(Instruction())
    def getInstructions(self):
        return self.instructions
    def numInstructions(self):
        return len(self.getInstructions())
    def showInstructions(self):
        for i in self.getInstructions():
            i.showInfo()

    def algoToASM(self):
        for instruction in self.getInstructions():
            print(instruction.toASM())
    def addInstruction(self,i):
        self.getInstructions().append(i)
    def copyBitInstructionWithMut(self,bitA,bitB,probMut):
        #choose between bitA and bitB
        bits = [bitA,bitB]
        res = str(bits[random.randint(0,1)])
        n = random.randint(1, 200)
        # mutation happend
        if n <= probMut:
            # type mutation
            typeMut = random.randint(1, 3)
            # change bit
            if typeMut == 1:
                if res == "0":
                    res == "1"
            elif typeMut == 2:
                #delete bit
                res = ""
            elif typeMut == 3:
                #add new bit
                res = res+str(random.randint(0,1))
        return res
    def crossInstruction(self,i1,i2,mutationProb=2):
        maxBits = i1.getMaxLenghtBits()
        codeRes = ""
        #mutation prob

        if maxBits > 32:
            maxBits = 32
        try:
            for i in range(maxBits):
                codeRes = codeRes + self.copyBitInstructionWithMut(i1.getCode()[i],i2.getCode()[i],mutationProb)
        except IndexError:
            for i in range(32):
                codeRes = codeRes + str(random.randint(0, 1))
        lenCode = len(codeRes)
        #complete code (if too much delete mutation occur
        #can break 32 bits instruction
        if lenCode < maxBits:
            for i in range(maxBits-lenCode):
                codeRes = codeRes + str(random.randint(0,1))
        if lenCode > maxBits:
            codeRes = codeRes[:maxBits]
        i = Instruction()
        i.setCode(codeRes)
        return i
    def cross(self,b,mutationProb=2):
        a = self
        numInstructionsA = len(self.getInstructions())
        numInstructionsB = len(b.getInstructions())
        if numInstructionsA < numInstructionsB:
            a,b = b, a
        newAlgorithm = Algorithm(instructions="empty")
        c = 0
        while c < len(b.getInstructions()):
            newAlgorithm.addInstruction(self.crossInstruction(a.getInstructions()[c], b.getInstructions()[c],mutationProb))
            c = c +1
        #check if there are more instructions in a algorithm and b algorithm not
        if c < len(a.getInstructions()):
            while c < len(a.getInstructions()):
                newAlgorithm.addInstruction(self.crossInstruction(a.getInstructions()[c], a.getInstructions()[c],mutationProb))
                c = c + 1
        return newAlgorithm
