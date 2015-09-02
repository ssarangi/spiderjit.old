from ir.module import *
from ir.function import *
from ir.instructions import *

from ir.base_ir_visitor import *
from ir.validator import *

class Frame:
    def __init__(self):
        self.__symbols = {}

    def add_to_frame(self, node, value):
        self.__symbols.update(node, value)

    def is_in_frame(self, node):
        if node in self.__symbols:
            return self.__symbols[node]
        
        return None

class IRVirtualMachine(IRBaseVisitor):
    def __init__(self):
        self.__global_frame = Frame()


    def __add_to_frame(self, name, value):
        self.__global_frame.update(name, value)

    def visit_module(self, node):
        for g in node.globals:
            self.__add_to_frame(g.name, g.initializer)

        visit(node.entry_point)

    def visit_function(self, node):
        raise NotImplementedError("Function not implemented")