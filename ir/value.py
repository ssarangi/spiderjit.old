__author__ = 'sarangis'

from ir.types import *

class Value:
    def __init__(self):
        pass

class Argument(Value):
    def __init__(self, type, name):
        Value.__init__(self)

        if not isinstance(name, str):
            raise InvalidTypeException("Expected a string")
        self.__name = name

        if not isinstance(type, BaseType):
            raise InvalidTypeException("Expected BaseType")

        self.__type = type

    @property
    def name(self):
        return self.name

    @property
    def type(self):
        return self.__type

    def __str__(self):
        output_str = str(self.__type) + " " + "%" + str(self.__name)
        return output_str

    __repr__ = __str__