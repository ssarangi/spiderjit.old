__author__ = 'sarangis'

from ir.instructions import *

def is_terminator_instruction(inst):
    if (isinstance(inst, TerminateInstruction) or
        isinstance(inst, ReturnInstruction) or
        isinstance(inst, BranchInstruction) or
        isinstance(inst, ConditionalBranchInstruction)):
        return True
    else:
        return False