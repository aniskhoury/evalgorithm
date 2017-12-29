# -*- coding: utf-8 -*-
DEBUG = False

from EVA import *
from structure.io import *
from features import *
from structure.virtualmachine import *
#generate 10 instructions
ins = [Instruction() for i in range(10)]

ins[0].generateCode("PUSH 0 3")
ins[1].generateCode("PUSH 1 2")
ins[2].generateCode("ANDmem 0 0 1")


algo = Algorithm(instructions=ins)
virtualm = VirtualMachine(64)
virtualm.loadAlgorithm(algo)
print ins[0].toASM()
print ins[1].toASM()
print ins[2].toASM()

virtualm.runAlgorithm([])
print virtualm.getMemory()

