__author__ = 'sarangis'

from ir.exceptions import *
from ir.types import *
import ir.instructions
from ir.validator import *
from ir.value import *

class Function(Validator):
    @verify(name=str, ftype=FunctionType)
    def __init__(self, name, ftype):
        self.__basic_blocks = []

        if not isinstance(name, str):
            raise InvalidTypeException("name is expected to be a string")

        self.__name = name

        if not isinstance(ftype, FunctionType):
            raise InvalidTypeException("Function Type expected")

        self.__ftype = ftype
        self.__arguments = [None] * len(ftype.arg_types)

    @property
    def basic_blocks(self):
        return self.__basic_blocks

    @basic_blocks.setter
    def basic_blocks(self, block):
        return self.__basic_blocks.append(block)

    @property
    def args(self):
        return self.__arguments

    @verify(arg=Argument)
    def insert_arg(self, arg, idx = None):
        if idx > len(self.__ftype.arg_types):
            raise InvalidUsageModel("Invalid argument type. Function supports %s arguments but argument to be "
                                    "added at index %s" % (len(self.__ftype.arg_types), idx))

        # Check the function type for the number of args
        arg_type_idx = -1
        if idx is None:
            # Check the length of the arguments.
            arg_type_idx = len(self.__arguments)
        else:
            arg_type_idx = idx

        print(arg_type_idx)
        # Now check if the index we got has the same type as the one in function type
        arg_type = self.__ftype.arg_types[arg_type_idx]
        # Make sure that the arg has the same type as the arg type
        print(type(arg_type))
        print(type(arg.type))
        if not isinstance(arg.type, arg_type):
            raise InvalidTypeException("Argument: " + str(arg) + " Expected: " + str(arg_type) + " Received: " + str(arg.type))

        # Validate the arg
        if not isinstance(arg, Argument):
            raise InvalidTypeException("Argument type expected")

        if idx is not None:
            # Check if the argument list is already that size
            if len(self.__arguments) > idx:
                self.__arguments.insert(idx, arg)
            else:
                current_len = len(self.__arguments)
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
            if count != len(self.__ftype.arg_types) - 1:
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