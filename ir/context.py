__author__ = 'sarangis'

class Context:
    """ The main context for Spider JIT. This will hold all the global information needed for the module being built.
    """
    def __init__(self):
        self.__variable_index = 0
        self.__named_variables = {}
