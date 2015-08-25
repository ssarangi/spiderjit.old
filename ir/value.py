__author__ = 'sarangis'

class Value:
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls is Value:
            raise TypeError("base class may not be instantiated")
        return object.__new__(cls, *args, **kwargs)