# -*- coding: utf-8 -*-
DEBUG = False

from EVA import *
from structure.io import *
from features import *
from structure.virtualmachine import *
#generate 10 instructions
ins = [Instruction() for i in range(10)]
ins[0].generateCode("PUTmemarg 0 0")
ins[1].generateCode("PUTmemarg 1 1")
ins[2].generateCode("ANDmem 2 1 0")
ins[3].generateCode("NOTmem 2 2")



algo = Algorithm(instructions=ins)
virtualm = VirtualMachine(64)
virtualm.loadAlgorithm(algo)
print ins[0].toASM()
print ins[1].toASM()
print ins[2].toASM()
print ins[3].toASM()

virtualm.runAlgorithm([0,0])
print virtualm.getMemory()

