__author__ = 'sarangis'

from ir.module import *
from ir.context import *
from ir.irbuilder import *

int32Ty = IntType(32)
floatTy = FloatType()

def main():
    ctx = Context()
    mod = Module("MyModule", ctx)
    irbuilder = IRBuilder(mod, ctx)
    f = irbuilder.create_function("test_fn", int32Ty, int32Ty, floatTy, floatTy)
    print(mod)
    print(f)

    # itype = IntType(32)
    # print(itype)
    # pointer = PointerType(itype, 2)
    # print(pointer)


if __name__ == "__main__":
    main()