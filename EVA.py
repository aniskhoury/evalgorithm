from structure.virtualmachine import *
from config.evaconfig import *

class EVA:
    virtualMachines = []
    config = None
    currentGen = 0
    def __init__(self,config,virtualMachines=None,fnFitness=None):
        self.welcomeMessage()
    #n -> Number of virtual machines created.
    def createVirtualMachine(self,n=1):
        self.virtualMachines.append(VirtualMachine(memory=512))
    def run(self):
        print("Code run here")
    def showResults(self):
        print("###############################")
        print("########### Results ###########")
        print("###############################")

    def welcomeMessage(self):
        print("################################################")
        print("####### Welcome to Evolutionary Algorithm ######")
        print("#######    Created by Anis Khoury Ribas   ######")
        print("################################################")
