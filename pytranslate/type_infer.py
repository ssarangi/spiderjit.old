__author__ = 'sarangis'

import string
from pyjit.nodes import *

def naming():
    k = 0
    while True:
        for a in string.ascii_lowercase:
            yield ("'" + a + str(k)) if (k > 0) else (a)

class InferType(object):
    def __init__(self):
        self.constraints = []
        self.env = {}
        self.names = naming()

    def fresh(self):
        return VarTy('$' + next(self.names))

    def visit(self, node):
        name = "visit_%s" % (type(node).__name__)
        if hasattr(self, name):
            return getattr(self, name)(node)
        else:
            return self.generic_visit(node)

    def visit_Func(self, node):
        arity = len(node.args)
        self.argTys = [self.fresh()  for v in node.args]
        self.retTy = VarTy("$retTy")
        for (arg, ty) in zip(node.args, self.argTys):
            arg.type = ty
            self.env[arg.id] = ty

        for n in node.body: self.visit(n)
        return FuncTy(self.argTys, self.retTy)

    def visit_Noop(self, node):
        return None

    def visit_LitInt(self, node):
        tv = self.fresh()
        node.type = tv
        return tv

    def visit_LitFloat(self, node):
        tv = self.fresh()
        node.type = tv
        return tv

    def visit_LitBool(self, node):
        tv = self.fresh()
        node.type = tv
        return tv

    def visit_Assign(self, node):
        ty = self.visit(node.val)
        if node.ref in self.env:
            # Subsequent uses of a variable must have same type
            self.constraints += [(ty, self.env[node.ref])]

        self.env[node.ref] = ty
        node.ref = ty
        return None

    def visit_Index(self, node):
        tv = self.fresh()
        ty = self.visit(node.val)
        ixty = self.visit(node.ix)
        self.constraints += [(ty, array(tv)), (ixty, int32)]
        return tv

    def visit_Prim(self, node):
        if node.fn == "shape#":
            return array(int32)
        elif node.fn == "mult#" or node.fn == "add#":
            tya = self.visit(node.args[0])
            tyb = self.visit(node.args[1])
            self.constraints += [(tya, tyb)]
            return tyb
        else:
            raise NotImplementedError

    def visit_Var(self, node):
        ty = self.env[node.id]
        node.type = ty
        return ty

    def visit_Return(self, node):
        ty = self.visit(node.val)
        self.constraints += [(ty, self.retTy)]

    def visit_Loop(self, node):
        self.env[node.var.id] = int32
        varTy = self.visit(node.var)
        begin = self.visit(node.begin)
        end = self.visit(node.end)
        self.constraints += [(varTy, int32), (begin, int64), (end, int32)]
        for n in node.body: self.visit(n)

    def generic_visit(self, node):
        raise NotImplementedError