__author__ = 'sarangis'

from ir.exceptions import *
from ir.types import *

class Function:
    def __init__(self, name, ftype):
        self.__basic_blocks = []

        if not isinstance(name, str):
            raise InvalidTypeException("name is expected to be a string")

        self.__name = name

        if not isinstance(ftype, FunctionType):
            raise InvalidTypeException("Function Type expected")

        self.__ftype = ftype

    @property
    def basic_blocks(self):
        return self.__basic_blocks

    @basic_blocks.setter
    def basic_blocks(self, block):
        return self.__basic_blocks.append(block)

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

        output_str += "}\n\n"
        return output_str

class BasicBlock:
    def __init__(self):
        pass