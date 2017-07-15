from structure.instruction import *
class Algorithm:
    instructions = []
    def __init__(self,instructions=None):
        if instructions != None:
            self.setInstructions(instructions)
        else:
            self.setInstructions([])
            #number of instructions per default
            self.generateRandomAlgorithm(3)

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
