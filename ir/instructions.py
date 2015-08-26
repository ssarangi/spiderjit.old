__author__ = 'sarangis'

from ir.value import *
from ir.types import *
from ir.utils import *

class InstructionList(list):
    def __init__(self, name_generator):
        list.__init__(self)
        self.__name_generator = name_generator

    def append(self, inst):
        if inst.needs_name:
            inst.name = self.__name_generator.generate(inst)

        list.append(self, inst)

    def insert(self, idx, inst):
        if inst.needs_name:
            inst.name = self.__name_generator.generate(inst)

        list.insert(self, idx, inst)


    def __add__(self, other):
        raise NotImplementedError("__add__ method not implemented for InstructionList")

class Instruction(Value):
    def __init__(self, parent=None, name=None, needs_name=True):
        Value.__init__(self)
        self.__parent = parent
        self.__inst_idx = -1
        self.__name = name
        self.__needs_name = needs_name

    @property
    def needs_name(self):
        return self.__needs_name

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, bb):
        self.__parent = bb

    @property
    def inst_idx(self):
        return self.__inst_idx

    @inst_idx.setter
    def inst_idx(self, v):
        self.__inst_idx = v

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n


class CallInstruction(Instruction):
    def __init__(self, func, arg_list, parent=None, name=None):
        Instruction.__init__(self, parent, name)
        self.__func = func

        # Verify the Args
        self.__func.verify_args(arg_list)
        self.__args = arg_list

    @property
    def function(self):
        return self.__func

    @property
    def args(self):
        return self.__args

    def __str__(self):
        functype = self.__func.type
        output_str = "call " + str(functype.ret_type) + " @" + self.__func.name

        output_str += render_list_with_parens(self.__args)

        return output_str

    __repr__ = __str__


class TerminateInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class ReturnInstruction(Instruction):
    def __init__(self, value=None, parent=None, name=None):
        Instruction.__init__(self, parent, name, needs_name=False)
        self.__value = value

    def __str__(self):
        if self.__value is None:
            output_str = "return void"
        else:
            output_str = "return " + str(self.__value)
        return output_str

    __repr__ = __str__

class SelectInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class LoadInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class StoreInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name, needs_name=False)

    def __str__(self):
        pass

    __repr__ = __str__


class BinOpInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class AllocaInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class PhiInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class BranchInstruction(Instruction):
    def __init__(self, bb, parent=None, name=None):
        Instruction.__init__(self, parent, name, needs_name=False)
        if not isinstance(bb, BasicBlock):
            raise InvalidTypeException("Expected a Basic Block type")

        self.__bb = bb

    def __str__(self):
        output_str = "br " + self.__bb.name
        return output_str

    __repr__ = __str__


class ConditionalBranchInstruction(BranchInstruction):
    def __init__(self, bb, parent=None, name=None):
        BranchInstruction.__init__(self, bb, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class IndirectBranchInstruction(BranchInstruction):
    def __init__(self, bb, parent=None, name=None):
        BranchInstruction.__init__(self, bb, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class SwitchInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class ForInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class WhileInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class DoInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class IfInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class ElseInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class EndifInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class SelectInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class CompareInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class CastInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class GEPInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class ExtractElementInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class InsertElementInstruction(Instruction):
    def __init__(self, parent=None, name=None):
        Instruction.__init__(self, parent, name)

    def __str__(self):
        pass

    __repr__ = __str__


class BasicBlock(Validator):
    def __init__(self, name, parent):
        self.__name = name
        self.__parent = parent
        self.__instructions = InstructionList(parent.name_generator)

    @property
    def name(self):
        return self.__name

    @property
    def instructions(self):
        return self.__instructions

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
            if i == inst:
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
            output_str += "\t"

            if i.name is not None:
                output_str += "%" + i.name + " = "

            output_str += str(i) + "\n"

        return output_str

    __repr__ = __str__