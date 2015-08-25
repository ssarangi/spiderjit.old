__author__ = 'sarangis'

from ir.types import *
from ir.function import *
from ir.context import *
from ir.module import *

class IRBuilder:
    """ The main builder to be used for creating instructions. This has to be used to insert / create / modify instructions
        This class will have to support all the other class creating it.
    """
    def __init__(self, current_module = None, context=None):
        self.__module = current_module
        self.__insertion_point = None
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

    @property
    def insertion_point(self):
        return self.__insertion_point

    @insertion_point.setter
    def insertion_point(self, ip):
        self.__insertion_point = ip


    def insert_instruction(function_to_decorate):
        def wrapper(*args, **kw):
            # Calling your function
            output = function_to_decorate(*args, **kw)
            # Below this line you can do post processing
            print("In Post Processing...." + output)
        return wrapper

    @insert_instruction
    def do_something(*args, **kwargs):
        if args[0] == 'foo':
            return 'bar'
        else:
            return 'baz'


    def create_function_type(self, ret_ty, *arg_tys):
        return FunctionType(ret_ty, *arg_tys)

    def create_function(self, name, *args):
        if (len(args) == 1 and isinstance(args[0], FunctionType)):
            return Function(name, args[0])
        else:
            ftype = self.create_function_type(args[0], *args[1:])
            return Function(name, ftype)
