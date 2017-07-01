numVirtualMachines = None
maxNumGenerations = 500
typeCross = 0
typeSelect = 0
numBitsInstruction = 32

class EVAconfig:
    numVirtualMachines = None
    numGeneration = 500
    mode = 1
    typeCross = 0
    typeSelect = 0
    numBitsInstruction = 32

    def __init__(self,numVirtualMachines = 1,maxNumGeneration = 500):
        self.initConfig()

    def getNumBitsInstruction(self):
        return self.numBitsInstruction
    def getTypeSelect(self):
        return self.typeSelect
    def getTypeCross(self):
        return self.typeCross
    def getMaxNumGenerations(self):
        return self.maxNumGeneration
    def getNumVirtualMachines(self):
        return self.numVirtualMachines
    def initGlobalConfig(self):
        global numBitsInstruction, typeCross, typeSelect, maxNumGenerations, numVirtualMachines
        numBitsInstruction = self.getNumBitsInstruction()
        typeCross = self.getTypeCross()
        typeSelect = self.getTypeSelect()
        maxNumGenerations = self.getMaxNumGenerations()
        numVirtualMachines = self.getNumVirtualMachines()