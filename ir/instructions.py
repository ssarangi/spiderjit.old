__author__ = 'sarangis'

from ir.value import *
from ir.types import *
from ir.utils import *

class Instruction(Value):
    def __init__(self):
        Value.__init__(self)
        self.__parent = None

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, bb):
        self.__parent = bb

class CallInstruction(Instruction):
    def __init__(self, func, *args):
        self.__func = func
        self.__args = args

    @property
    def function(self):
        return self.__func

    @property
    def args(self):
        return self.__args

class TerminateInstruction(Instruction):
    def __init__(self):
        pass

class ReturnInstruction(Instruction):
    def __init__(self):
        pass

    def __str__(self):
        output_str = "return void"
        return output_str

    __repr__ = __str__

class SelectInstruction(Instruction):
    def __init__(self):
        pass

class LoadInstruction(Instruction):
    def __init__(self):
        pass

class StoreInstruction(Instruction):
    def __init__(self):
        pass

class BinOpInstruction(Instruction):
    def __init__(self):
        pass

class AllocaInstruction(Instruction):
    def __init__(self):
        pass

class PhiInstruction(Instruction):
    def __init__(self):
        pass

class BranchInstruction(Instruction):
    def __init__(self, bb):
        if not isinstance(bb, BasicBlock):
            raise InvalidTypeException("Expected a Basic Block type")

        self.__bb = bb

    def __str__(self):
        output_str = "br " + self.__bb.name
        return output_str

    __repr__ = __str__

class ConditionalBranchInstruction(BranchInstruction):
    def __init__(self):
        pass

class IndirectBranchInstruction(BranchInstruction):
    def __init__(self):
        pass

class SwitchInstruction(Instruction):
    def __init__(self):
        pass

class ForInstruction(Instruction):
    def __init__(self):
        pass

class WhileInstruction(Instruction):
    def __init__(self):
        pass

class DoInstruction(Instruction):
    def __init__(self):
        pass

class IfInstruction(Instruction):
    def __init__(self):
        pass

class ElseInstruction(Instruction):
    def __init__(self):
        pass

class EndifInstruction(Instruction):
    def __init__(self):
        pass

class SelectInstruction(Instruction):
    def __init__(self):
        pass

class CompareInstruction(Instruction):
    def __init__(self):
        pass

class CastInstruction(Instruction):
    def __init__(self):
        pass

class GEPInstruction(Instruction):
    def __init__(self):
        pass

class ExtractElementInstruction(Instruction):
    def __init__(self):
        pass

class InsertElementInstruction(Instruction):
    def __init__(self):
        pass

class BasicBlock(Validator):
    def __init__(self, name):
        self.__name = name
        self.__instructions = []
        self.parent = None

    @property
    def name(self):
        return self.__name

    @property
    def instructions(self):
        return self.__instructions

    @instructions.setter
    def instructions(self, inst):
        self.__instructions.append(inst)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, bb):
        self.__parent = bb

    @verify(inst=Instruction)
    def find_instruction_idx(self, inst):
        if not isinstance(inst, Instruction):
            raise InvalidTypeException("Expected an Instruction Type")

        for idx, i in enumerate(self.__instructions):
            if (i == inst):
                return idx

        return None

    def validate(self):
        error_str = self.__name + " BB has not terminator instruction"
        # Get the last instruction and make sure its the terminator
        if len(self.__instructions) > 0:
            last_inst = self.__instructions[len(self.__instructions) - 1]
            if not is_terminator_instruction(last_inst):
                raise NoBBTerminatorException(error_str)
        else:
            raise NoBBTerminatorException(error_str)

    def __str__(self):
        output_str = self.name + ":\n"
        for i in self.__instructions:
            output_str += "\t" + str(i) + "\n"

        return output_str

    __repr__ = __str__