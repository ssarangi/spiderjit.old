from utils.base_visitor import *

class IRBaseVisitor(BaseVisitor):
    def __init__(self, node):
        pass

    def visit_module(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_function(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_callinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_terminateinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_returninstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_selectinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_loadinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_storeinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_addinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)
    
    def visit_subinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_mulinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_divinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_faddinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_fsubinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_fmulinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_fdivinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_allocainstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_phiinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_conditionalbranchinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_indirectbranchinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_switchinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)
    
    def visit_selectinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_icmpinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_fcmpinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_castinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_gepinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_extractelementinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_insertelementinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_shiftleftinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_logicalshiftrightinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_arithmeticshiftrightinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_andinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_orinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_xorinstruction(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)

    def visit_basicblock(self, node):
        raise NotImplementedError("IR Node not implemented: visit_%s" % type(node).__name__)