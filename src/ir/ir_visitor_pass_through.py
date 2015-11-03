"""
The MIT License (MIT)

Copyright (c) 2015 <Satyajit Sarangi>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from utils.base_visitor import *

class IRVisitorPassthrough(BaseVisitor):
    def __init__(self):
        BaseVisitor.__init__(self)
        pass

    def visit_module(self, node):
        pass

    def visit_function(self, node, arg_list=None):
        pass

    def visit_basicblock(self, node):
        pass

    def visit_callinstruction(self, node):
        pass

    def visit_terminateinstruction(self, node):
        pass

    def visit_returninstruction(self, node):
        pass

    def visit_selectinstruction(self, node):
        pass

    def visit_loadinstruction(self, node):
        pass

    def visit_storeinstruction(self, node):
        pass

    def visit_addinstruction(self, node):
        pass

    def visit_subinstruction(self, node):
        pass

    def visit_mulinstruction(self, node):
        pass

    def visit_divinstruction(self, node):
        pass

    def visit_faddinstruction(self, node):
        pass

    def visit_fsubinstruction(self, node):
        pass

    def visit_fmulinstruction(self, node):
        pass

    def visit_fdivinstruction(self, node):
        pass

    def visit_allocainstruction(self, node):
        pass

    def visit_phiinstruction(self, node):
        pass

    def visit_conditionalbranchinstruction(self, node):
        pass

    def visit_indirectbranchinstruction(self, node):
        pass

    def visit_switchinstruction(self, node):
        pass

    def visit_icmpinstruction(self, node):
        pass

    def visit_fcmpinstruction(self, node):
        pass

    def visit_castinstruction(self, node):
        pass

    def visit_gepinstruction(self, node):
        pass

    def visit_extractelementinstruction(self, node):
        pass

    def visit_insertelementinstruction(self, node):
        pass

    def visit_shiftleftinstruction(self, node):
        pass

    def visit_logicalshiftrightinstruction(self, node):
        pass

    def visit_arithmeticshiftrightinstruction(self, node):
        pass

    def visit_andinstruction(self, node):
        pass

    def visit_orinstruction(self, node):
        pass

    def visit_xorinstruction(self, node):
        pass