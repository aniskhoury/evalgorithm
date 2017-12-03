from EVA import *
class IO:
    input = []
    output = []
    result = []


    def addTest(self,input,output,result):
        self.input.append(input)
        self.output.append(output)
        self.result.append(result)

    def addInputArgument(self,e):
        self.getInput().append(e)
    def addOutputArgument(self,o):
        self.getOutput().append(o)
    def addResultArgument(self,r):
        self.getResult().append(r)
    def getInput(self):
        return self.input
    def getOutput(self):
        return self.output
    def getResult(self):
        return self.result