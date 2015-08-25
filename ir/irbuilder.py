__author__ = 'sarangis'

from ir.types import *
from ir.function import *
from ir.context import *
from ir.module import *
from ir.instructions import *
from ir.basicblock import *

class IRBuilder:
    """ The main builder to be used for creating instructions. This has to be used to insert / create / modify instructions
        This class will have to support all the other class creating it.
    """
    def __init__(self, current_module = None, context=None):
        self.__module = current_module
        self.__insertion_point = None
        self.__insertion_point_idx = 0
        self.__orphaned_instructions = []
        self.__context = context

    @property
    def module(self):
        return self.__module

    @module.setter
    def module(self, mod):
        self.__module = mod

    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, ctx):
        self.__context = ctx

    def insert_after(self, ip):
        if isinstance(ip, BasicBlock):
            self.__insertion_point = ip
            self.__insertion_point_idx = 0
        elif isinstance(ip, Instruction):
            self.__insertion_point = ip
            self.__insertion_point_idx = ip.parent.find_instruction_idx(ip)
            if self.__insertion_point_idx == None:
                raise InvalidInstructionException("Count not find instruction in its parent basic block")
            else:
                self.__insertion_point_idx += 1
        else:
            raise InvalidTypeException("Expected either Basic Block or Instruction")

    def insert_before(self, ip):
        if isinstance(ip, BasicBlock):
            self.__insertion_point = ip
            self.__insertion_point_idx = -1
        elif isinstance(ip, Instruction):
            self.__insertion_point = ip
            self.__insertion_point_idx = ip.parent.find_instruction_idx(ip)
            if self.__insertion_point_idx == None:
                raise InvalidInstructionException("Count not find instruction in its parent basic block")
            elif self.__insertion_point_idx == 0:
                self.__insertion_point_idx = 0
            else:
                self.__insertion_point_idx -= 1
        else:
            raise InvalidTypeException("Expected either Basic Block or Instruction")

    # @classmethod
    # def insert_instruction(instruction_creator):
    #     def wrapper(self, *args, **kw):
    #         # Calling your function
    #         output = instruction_creator(*args, **kw)
    #
    #         # Now check the insertion point and add the instruction accordingly
    #         if self.__insertion_point_idx == -1:
    #             # This is an orphaned instruction
    #             self.__orphaned_instructions.append(output)
    #
    #     return wrapper
    #
    # @insert_instruction
    # def do_something(*args, **kwargs):
    #     if args[0] == 'foo':
    #         return 'bar'
    #     else:
    #         return 'baz'
    def __add_instruction(self, inst):
        if self.__insertion_point_idx == -1:
            # This is an orphaned instruction
            self.__orphaned_instructions.append(inst)
        elif isinstance(self.__insertion_point, BasicBlock):
            self.__insertion_point.instructions.append(inst)
            self.__insertion_point = inst
        elif isinstance(self.__insertion_point, Instruction):
            bb = self.__insertion_point.parent
            bb.instructions.insert(self.__insertion_point_idx, inst)

            self.__insertion_point_idx += 1
            self.__insertion_point = inst
        else:
            raise Exception("Could not add instruction")

    def create_function_type(self, ret_ty, *arg_tys):
        return FunctionType(ret_ty, *arg_tys)

    def create_function(self, name, *args):
        if (len(args) == 1 and isinstance(args[0], FunctionType)):
            return Function(name, args[0])
        else:
            ftype = self.create_function_type(args[0], *args[1:])
            return Function(name, ftype)

    def create_basic_block(self, name):
        return BasicBlock(name)

    def create_return(self, value = None):
        ret_inst = ReturnInstruction()
        self.__add_instruction(ret_inst)

    def create_branch(self, bb):
        if not isinstance(bb, BasicBlock):
            raise InvalidTypeException("Expected a Basic Block")

        branch_inst = BranchInstruction(bb)
        self.__add_instruction(branch_inst)
