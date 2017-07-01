class Algorithm:
    instructions = None
    def __init__(self,instructions=None):
            self.initInstructions(instructions)
    def initInstructions(self,i=None):
        if i == None:
            self.instructions = list()
        else:
            self.instructions = i
    def numInstructions(self):
        return len()