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

    arg4 = Argument(int32Ty, "myarg")
    f.insert_arg(arg4, 6)
    print(f.args)

    bb = irbuilder.create_basic_block("entry")
    f.basic_blocks.append(bb)
    bb_exit = irbuilder.create_basic_block("exit")
    f.basic_blocks.append(bb_exit)

    irbuilder.insert_after(bb)
    irbuilder.create_branch(bb_exit)

    irbuilder.insert_after(bb_exit)
    irbuilder.create_return()

    mod.functions.append(f)
    mod.validate()

    print(mod)

    # itype = IntType(32)
    # print(itype)
    # pointer = PointerType(itype, 2)
    # print(pointer)


if __name__ == "__main__":
    # main()
    test_verify("name")