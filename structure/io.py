from EVA import *
class IO:
    input = []
    output = []
    result = []
    def __init__(self,input=[],output=[],result=[]):
        global DEBUG
        print("Debug",DEBUG)
        self.setInput(input)
        self.setOutput(output)
        self.setResult(result)
    def addTest(self,input,output,result):
        self.addInputArgument(input)
        self.addOutputArgument(output)
        self.addResultArgument(result)
    def setInput(self,i):
        self.input = i
    def setOutput(self,o):
        self.output = o
    def setResult(self,r):
        self.result = r
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