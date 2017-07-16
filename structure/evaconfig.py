numVirtualMachines = None
numGenerations = 500
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
    population = 100
    io = None
    def __init__(self,io,numGenerations=800, numVirtualMachines=1, typeCross=0, population=100):
        self.setNumGenerations(numGenerations)
        self.setNumVirtualMachines(numVirtualMachines)
        self.setTypeCross(typeCross)
        self.setPopulation(population)
        self.initGlobalConfig()
        self.setIO(io)
    def setIO(self,io):
        self.io = io
    def getIO(self):
        return self.io
    def setNumGenerations(self,n):
        self.numGenerations = n
    def setNumVirtualMachines(self,n):
        self.numVirtualMachines = n
    def setTypeCross(self,n):
        self.typeCross = n
    def setPopulation(self,n):
        self.population = n
    def getNumBitsInstruction(self):
        return self.numBitsInstruction
    def getTypeSelect(self):
        return self.typeSelect
    def getTypeCross(self):
        return self.typeCross
    def getNumGenerations(self):
        return self.numGenerations
    def getNumVirtualMachines(self):
        return self.numVirtualMachines
    def getPopulation(self):
        return self.population
    def initGlobalConfig(self):
        global numBitsInstruction, typeCross, typeSelect, numGenerations, numVirtualMachines,population
        numBitsInstruction = self.getNumBitsInstruction()
        typeCross = self.getTypeCross()
        typeSelect = self.getTypeSelect()
        numGeneration = self.getNumGenerations()
        numVirtualMachines = self.getNumVirtualMachines()
        population = self.getPopulation()