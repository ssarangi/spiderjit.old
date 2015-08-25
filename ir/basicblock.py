__author__ = 'sarangis'

from ir.instructions import *
from ir.validator import *
from ir.exceptions import *
from ir.utils import *

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
        if (len(self.__instructions) > 0):
            last_inst = self.__instructions[len(self.__instructions) - 1]
            if (not is_terminator_instruction(last_inst)):
                raise NoBBTerminatorException(error_str)
        else:
            raise NoBBTerminatorException(error_str)

    def __str__(self):
        output_str = self.name + ":\n"
        for i in self.__instructions:
            output_str += "\t" + str(i) + "\n"

        return output_str

    __repr__ = __str__