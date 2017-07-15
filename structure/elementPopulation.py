class elementPopulation:

    algorithm = None
    score = None
    def __init__(self,algorithm=None,score=None):
        self.setAlgorithm(algorithm)
        self.setScore(score)
        
    def setAlgorithm(self,a):
        self.algorithm = a
    def setScore(self,s):
        self.score = s
    def getAlgorithm(self):
        return self.algorithm
    def getScore(self):
        if self.score == None:
            return 0
        return self.score
    def showElement(self):
        if self.getAlgorithm() != None:
            print("#####################")
            print("Show Element")
            print("num instructions:",len(self.getAlgorithm().getInstructions()))
            for i in self.getAlgorithm().getInstructions():
                i.showInfo()
            exit()
            print("Score:",self.getScore())
            print("#####################")
