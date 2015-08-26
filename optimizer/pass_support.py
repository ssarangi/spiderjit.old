__author__ = 'sarangis'

from ir.exceptions import *

class ModulePass:
    def __init__(self):
        pass

    def run_on_module(self):
        raise NotImplementedError("Derived passes class should implement run_on_module")

class FunctionPass:
    def __init__(self):
        pass

    def run_on_function(self):
        raise NotImplementedError("Derived passes class should implement run_on_function")