__author__ = 'sarangis'

from pyjit.visitors import *
from pyjit.type_infer import *
from pyjit.pretty_print import *

def autojit(fn):
    transformer = PythonVisitor()
    core = transformer(fn)
    infer = InferType()
    sig = infer.visit(core)
    print('Signature:%s \n' % sig)

    print('Constraints:')
    for (a,b) in infer.constraints:
        print(a, '~', b)

    print(pformat_ast(core))
