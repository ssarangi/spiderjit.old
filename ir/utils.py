__author__ = 'sarangis'

import ir.instructions

def is_terminator_instruction(inst):
    if (isinstance(inst, ir.instructions.TerminateInstruction) or
        isinstance(inst, ir.instructions.ReturnInstruction) or
        isinstance(inst, ir.instructions.BranchInstruction) or
        isinstance(inst, ir.instructions.ConditionalBranchInstruction)):
        return True
    else:
        return False