__author__ = 'sarangis'

from ir.exceptions import *
from ir.types import *
from ir.instructions import *
from ir.validator import *

class Function(Validator):
    def __init__(self, name, ftype):
        self.__basic_blocks = []

        if not isinstance(name, str):
            raise InvalidTypeException("name is expected to be a string")

        self.__name = name

        if not isinstance(ftype, FunctionType):
            raise InvalidTypeException("Function Type expected")

        self.__ftype = ftype
        self.__arguments = []

    @property
    def basic_blocks(self):
        return self.__basic_blocks

    @basic_blocks.setter
    def basic_blocks(self, block):
        return self.__basic_blocks.append(block)

    @property
    def args(self):
        return self.__arguments

    def insert_arg(self, arg, idx = None):
        # Validate the arg
        if not isinstance(arg, Argument):
            raise InvalidTypeException("Argument type expected")

        if idx != None:
            # Check if the argument list is already that size
            if (len(self.__arguments) > idx):
                self.__arguments.insert(idx, arg)
            else:
                current_len = len(self.__arguments)
                for i in range(current_len, idx - 1):
                    self.__arguments.append(None)
                self.__arguments.append(arg)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    def __str__(self):
        output_str = ""
        output_str += "define " + str(self.__ftype.ret_type) + " " + self.__name + "("

        for count, arg_ty in enumerate(self.__ftype.arg_types):
            output_str += str(arg_ty)
            if (count != len(self.__ftype.arg_types) - 1):
                output_str += ", "

        output_str += ") {\n"

        # render each basic block
        for bb in self.__basic_blocks:
            output_str += str(bb)

        output_str += "}\n\n"
        return output_str

    def validate(self):
        for bb in self.__basic_blocks:
            bb.validate()

    __repr__ = __str__