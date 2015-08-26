__author__ = 'sarangis'

from ir.module import *
from ir.context import *
from ir.irbuilder import *
from ir.constants import *

int32Ty = IntType(32)
floatTy = FloatType()

def main():
    ctx = Context()
    mod = Module("MyModule", ctx)
    irbuilder = IRBuilder(mod, ctx)

    ft = irbuilder.create_function_type(int32Ty, floatTy, floatTy)
    f = irbuilder.create_function("test_fn", ft)

    ft1 = irbuilder.create_function_type(int32Ty, int32Ty, int32Ty)
    f1 = irbuilder.create_function("foo", ft1)

    arg0 = Argument(floatTy, "myarg")
    arg1 = Argument(floatTy, "myarg1")
    f.args = [arg0, arg1]

    arg2 = Argument(int32Ty, "a")
    arg3 = Argument(int32Ty, "b")
    f1.args = [arg2, arg3]

    bb = irbuilder.create_basic_block("entry", f)
    f.basic_blocks.append(bb)
    bb_exit = irbuilder.create_basic_block("exit", f)
    f.basic_blocks.append(bb_exit)

    irbuilder.insert_after(bb)
    irbuilder.create_call(f1, IntConstant(32, 5), IntConstant(32, 3))
    irbuilder.create_call(f1, IntConstant(32, 7), IntConstant(32, 2), name="call")
    irbuilder.create_call(f1, IntConstant(32, 9), IntConstant(32, 1), name="call")
    irbuilder.create_fadd(IntConstant(32, 4), IntConstant(32, 7))
    irbuilder.create_branch(bb_exit)

    irbuilder.insert_after(bb_exit)
    irbuilder.create_return()

    mod.functions.append(f)
    mod.functions.append(f1)
    print(mod)
    mod.validate()


if __name__ == "__main__":
    main()
