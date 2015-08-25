__author__ = 'sarangis'

from ir.value import *

class Constant(Value):
    def __init__(self):
        Value.__init__(self)

    def __new__(cls, *args, **kwargs):
        if cls is Constant:
            raise TypeError("base class may not be instantiated")
        return object.__new__(cls, *args, **kwargs)

class IntConstant(Constant):
    def __init__(self):
        Constant.__init__(self)

class FloatConstant(Constant):
    def __init__(self):
        Constant.__init__(self)

class DoubleConstant(Constant):
    def __init__(self):
        Constant.__init__(self)

class StrConstant(Constant):
    def __init__(self):
        Constant.__init__(self)
