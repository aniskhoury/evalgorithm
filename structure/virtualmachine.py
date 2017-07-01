class VirtualMachine:
    memory = None
    algorithm = None
    pc = None #program counter
    def __init__(self,memory=1024,algorithm = None,pc = None):
        if memory == None:
            self.setMemory(list())
        if algorithm == None:
            self.setPc()

    def setMemory(self,m):
        self.memory = m
    def getNextInstruction(self):
        pc = self.getPc()
        if pc != None:
            pc = pc +1
            if pc > -1 and pc <= len()
        return False
    def runAlgorithm(self):
        algorithm = self.getAlgorithm()
        if algorithm == None:
            return False


        return True

    def loadAlgorithm(self,a):
        self.algorithm = a
    def getAlgorithm(self):
        return self.algorithm
    def setPc(self,pc):
        if len(self.getAlgorithm()) == 0 or pc == None or pc < 0 or pc >= len(self.getAlgorithm()):
            self.pc = None
        else:
            self.pc =
    def getPc(self):
        return self.pc