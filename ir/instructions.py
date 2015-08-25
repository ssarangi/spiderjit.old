__author__ = 'sarangis'

class Instruction(Value):
    def __init__(self):
        Value.__init__(self)

    def __new__(cls, *args, **kwargs):
        if cls is Instruction:
            raise TypeError("base class may not be instantiated")
        return object.__new__(cls, *args, **kwargs)

class CallInstruction(Instruction):
    def __init__(self, func, *args):
        self.__func = func
        self.__args = args

    @property
    def function(self):
        return self.__func

    @property
    def args(self):
        return self.__args

class TerminateInstruction(Instruction):
    def __init__(self):
        pass

class ReturnInstruction(Instruction):
    def __init__(self):
        pass

    def __str__(self):
        output_str = "ret"
        return output_str

class SelectInstruction(Instruction):
    def __init__(self):
        pass

class LoadInstruction(Instruction):
    def __init__(self):
        pass

class StoreInstruction(Instruction):
    def __init__(self):
        pass

class BinOpInstruction(Instruction):
    def __init__(self):
        pass

class AllocaInstruction(Instruction):
    def __init__(self):
        pass

class PhiInstruction(Instruction):
    def __init__(self):
        pass

class BranchInstruction(Instruction):
    def __init__(self):
        pass

class ConditionalBranchInstruction(BranchInstruction):
    def __init__(self):
        pass

class IndirectBranchInstruction(BranchInstruction):
    def __init__(self):
        pass

class SwitchInstruction(Instruction):
    def __init__(self):
        pass

class ForInstruction(Instruction):
    def __init__(self):
        pass

class WhileInstruction(Instruction):
    def __init__(self):
        pass

class DoInstruction(Instruction):
    def __init__(self):
        pass

class IfInstruction(Instruction):
    def __init__(self):
        pass

class ElseInstruction(Instruction):
    def __init__(self):
        pass

class EndifInstruction(Instruction):
    def __init__(self):
        pass

class SelectInstruction(Instruction):
    def __init__(self):
        pass

class CompareInstruction(Instruction):
    def __init__(self):
        pass

class CastInstruction(Instruction):
    def __init__(self):
        pass

class GEPInstruction(Instruction):
    def __init__(self):
        pass

class ExtractElementInstruction(Instruction):
    def __init__(self):
        pass

class InsertElementInstruction(Instruction):
    def __init__(self):
        pass
