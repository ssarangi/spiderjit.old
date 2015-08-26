__author__ = 'sarangis'

from ir.value import *

class Constant(Value):
    def __init__(self):
        Value.__init__(self)

class IntConstant(Constant):
    def __init__(self, bits, initializer):
        Constant.__init__(self)
        self.__type = IntType(bits)
        self.__initializer = initializer

    @property
    def type(self):
        return self.__type

class FloatConstant(Constant):
    def __init__(self, initializer):
        Constant.__init__(self)
        self.__initializer = initializer

    @property
    def type(self):
        return self.__type


class DoubleConstant(Constant):
    def __init__(self, initializer):
        Constant.__init__(self)
        self.__initializer = initializer

    @property
    def type(self):
        return self.__type


class StrConstant(Constant):
    def __init__(self):
        Constant.__init__(self)

    @property
    def type(self):
        return self.__type
