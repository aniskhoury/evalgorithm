class Algorithm:
    instructions = None
    def __init__(self,instructions=None):
            self.initInstructions(instructions)
    def initInstructions(self,i=None):
        if i == None:
            self.instructions = list()
        else:
            self.instructions = i
    def getInstructions(self):
        return self.instructions
    def numInstructions(self):
        return len(self.getInstructions())
    def showInstructions(self):
        for i in self.getInstructions():
            i.showInfo()