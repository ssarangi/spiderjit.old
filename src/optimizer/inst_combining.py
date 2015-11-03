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

from optimizer.pass_support import FunctionPass
from ir.validator import verify
from ir.function import Function
from ir.ir_visitor_pass_through import IRVisitorPassthrough

class InstCombine(FunctionPass, IRVisitorPassthrough):
    def __init__(self):
        FunctionPass.__init__(self)

    @verify(node=Function)
    def run_on_function(self, node):
        self.visit(node)

    @verify(node=Function)
    def visit_function(self, node, arg_list=None):
        for bb in node.basic_blocks():
            self.visit(bb)

    def visit_basicblock(self, node):
        for i in node:
            self.visit(i)

    def visit_addinstruction(self, node):
        """
        Try to detect i += constant
        :param node: add instruction
        :return: None
        """
        node.print()

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