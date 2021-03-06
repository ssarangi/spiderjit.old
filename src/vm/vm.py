﻿import dis
import operator

# Very good explanation comes from this link. https://ep2013.europython.eu/conference/talks/all-singing-all-dancing-python-bytecode

uninitialized = None

COMPARE_OPERATORS = [
    operator.lt,
    operator.le,
    operator.eq,
    operator.ne,
    operator.gt,
    operator.ge,
    lambda x, y: x in y,
    lambda x, y: x not in y,
    lambda x, y: x is y,
    lambda x, y: x is not y,
    lambda x, y: issubclass(x, Exception) and issubclass(x, y),
    ]

class BytecodeVM:
    def __init__(self, fn, *args):
        self.__code_object = fn.__code__
        self.__constants = self.__code_object.co_consts
        self.__names = self.__code_object.co_names
        self.__program = self.__code_object.co_code
        self.__nlocals = self.__code_object.co_nlocals

        self.__globals_dict = fn.__globals__
        self.__builtins_dict = self.__globals_dict['__builtins__']

        self.__ip = 0
        self.__locals = []
        if isinstance(args, list):
            self.__locals += args
        else:
            self.__locals += list(args)
        self.__locals += [uninitialized] * (self.__nlocals - len(args))
        self.__stack = []
        self.__value = None

    @property
    def value(self):
        return self.__value

    def print_members(self):
        co_methods = [method for method in dir(self.__code_object) if method.startswith("co_")]
    
        for method in co_methods:
            m = getattr(self.__code_object, method)
            print("Calling method: %s" % method)
            print(m)

    def _generate_opcode(self):
        bytecode = self.__code_object.co_code
        extended_arg = 0
        i = 0
        n = len(bytecode)
        while i < n:
            op = bytecode[i]
            i += 1
            if op >= dis.HAVE_ARGUMENT:
                # when opcodes have arguments, the next 2 bytes represent the args.
                # the first byte is the LSB and the 2nd byte is the MSB. So the MSB 
                # has to be shifted by 8 bits
                oparg = bytecode[i] | (bytecode[i+1] << 8) + extended_arg
                extended_arg = 0
                i += 2
                if op == dis.EXTENDED_ARG:
                    extended_arg = oparg * 65536
                    continue
            else:
                oparg = None

            yield(op, oparg)

    def execute(self):
        while True:
            op = self.__program[self.__ip]
            self.__ip += 1
            opmethod = "execute_%s" % dis.opname[op]

            if op >= dis.HAVE_ARGUMENT:
                low = self.__program[self.__ip]
                high = self.__program[self.__ip + 1]
                oparg = (high << 8) | low
                self.__ip += 2

            if (hasattr(self, opmethod)):
                terminate = getattr(self, opmethod)(oparg)
                if terminate:
                    break
            else:
                raise NotImplementedError("Method %s not found." % (opmethod))

    def execute_NOP(self, oparg):
        """
        Do nothing code. Used as a placeholder by the bytecode optimizer.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_POP_TOP(self, oparg):
        """
        Removes the top-of-stack (TOS) item.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_ROT_TWO(self, oparg):
        """
        Swaps the two top-most stack items.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_ROT_THREE(self, oparg):
        """
        Lifts second and third stack item one position up, moves top down to position three.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_DUP_TOP(self, oparg):
        """
        Duplicates the reference on top of the stack.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_DUP_TOP_TWO(self, oparg):
        """
        Duplicates the two references on top of the stack, leaving them in the same order.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    # Unary operations
    # Unary operations take the top of the stack, apply the operation, and push the result back on the stack.

    def execute_UNARY_POSITIVE(self, oparg):
        """
        Implements TOS = +TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_UNARY_NEGATIVE(self, oparg):
        """
        Implements TOS = -TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_UNARY_NOT(self, oparg):
        """
        Implements TOS = not TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_UNARY_INVERT(self, oparg):
        """
        Implements TOS = ~TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_GET_ITER(self, oparg):
        """
        Implements TOS = iter(TOS).
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    # Binary operations
    # Binary operations remove the top of the stack (TOS) and the second top-most stack item (TOS1) from the stack.
    # They perform the operation, and put the result back on the stack.

    def execute_BINARY_POWER(self, oparg):
        """
        Implements TOS = TOS1 ** TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_BINARY_MULTIPLY(self, oparg):
        """
        Implements TOS = TOS1 * TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BINARY_FLOOR_DIVIDE(self, oparg):
        """
        Implements TOS = TOS1 // TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BINARY_TRUE_DIVIDE(self, oparg):
        """
        Implements TOS = TOS1 / TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BINARY_MODULO(self, oparg):
        """
        Implements TOS = TOS1 % TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BINARY_ADD(self, oparg):
        """
        Implements TOS = TOS1 + TOS.
        """
        w = self.__stack.pop()
        v = self.__stack.pop()
        self.__stack.append(v + w)


    def execute_BINARY_SUBTRACT(self, oparg):
        """
        Implements TOS = TOS1 - TOS.
        """
        w = self.__stack.pop()
        v = self.__stack.pop()
        self.__stack.append(v - w)

    def execute_BINARY_SUBSCR(self, oparg):
        """
        Implements TOS = TOS1[TOS].
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BINARY_LSHIFT(self, oparg):
        """
        Implements TOS = TOS1 << TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BINARY_RSHIFT(self, oparg):
        """
        Implements TOS = TOS1 >> TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BINARY_AND(self, oparg):
        """
        Implements TOS = TOS1 & TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BINARY_XOR(self, oparg):
        """
        Implements TOS = TOS1 ^ TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BINARY_OR(self, oparg):
        """
        Implements TOS = TOS1 | TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    # In-place operations
    # In-place operations are like binary operations, in that they remove TOS and TOS1, and push
    # the result back on the stack, but the operation is done in-place when TOS1 supports it, and
    # the resulting TOS may be (but does not have to be) the original TOS1.

    def execute_INPLACE_POWER(self, oparg):
        """
        Implements in-place TOS = TOS1 ** TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_INPLACE_MULTIPLY(self, oparg):
        """
        Implements in-place TOS = TOS1 * TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_INPLACE_FLOOR_DIVIDE(self, oparg):
        """
        Implements in-place TOS = TOS1 // TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_INPLACE_TRUE_DIVIDE(self, oparg):
        """
        Implements in-place TOS = TOS1 / TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_INPLACE_MODULO(self, oparg):
        """
        Implements in-place TOS = TOS1 % TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_INPLACE_ADD(self, oparg):
        """
        Implements in-place TOS = TOS1 + TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_INPLACE_SUBTRACT(self, oparg):
        """
        Implements in-place TOS = TOS1 - TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_INPLACE_LSHIFT(self, oparg):
        """
        Implements in-place TOS = TOS1 << TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_INPLACE_RSHIFT(self, oparg):
        """
        Implements in-place TOS = TOS1 >> TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_INPLACE_AND(self, oparg):
        """
        Implements in-place TOS = TOS1 & TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_INPLACE_XOR(self, oparg):
        """
        Implements in-place TOS = TOS1 ^ TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_INPLACE_OR(self, oparg):
        """
        Implements in-place TOS = TOS1 | TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_STORE_SUBSCR(self, oparg):
        """
        Implements TOS1[TOS] = TOS2.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_DELETE_SUBSCR(self, oparg):
        """
        Implements del TOS1[TOS].
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    # Miscellaneous opcodes

    def execute_PRINT_EXPR(self, oparg):
        """
        Implements the expression statement for the interactive mode. TOS is removed from the
        stack and printed. In non-interactive mode, an expression statement is terminated with POP_TOP.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BREAK_LOOP(self, oparg):
        """
        Terminates a loop due to a break statement.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_CONTINUE_LOOP(self, target):
        """
        Continues a loop due to a continue statement. target is the address to jump to (which should be
        a FOR_ITER instruction).
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_SET_ADD(self, i):
        """
        Calls set.add(TOS1[-i], TOS). Used to implement set comprehensions.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_LIST_APPEND(self, i):
        """
        Calls list.append(TOS[-i], TOS). Used to implement list comprehensions.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_MAP_ADD(self, i):
        """
        Calls dict.setitem(TOS1[-i], TOS, TOS1). Used to implement dict comprehensions.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    # For all of the SET_ADD, LIST_APPEND and MAP_ADD instructions, while the added value or key/value pair
    # is popped off, the container object remains on the stack so that it is available for further iterations of the loop.

    def execute_RETURN_VALUE(self, oparg):
        """
        Returns with TOS to the caller of the function.
        """
        assert len(self.__stack) == 1
        self.__value = self.__stack[0]
        terminate = True
        return terminate

    def execute_YIELD_VALUE(self):
        """
        Pops TOS and yields it from a generator.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_YIELD_FROM(self):
        """
        Pops TOS and delegates to it as a subiterator from a generator.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    # New in version 3.3.

    def execute_IMPORT_STAR(self):
        """
        Loads all symbols not starting with '_' directly from the module TOS to the local namespace.
        The module is popped after loading all names. This opcode implements from module import *.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_POP_BLOCK(self):
        """
        Removes one block from the block stack. Per frame, there is a stack of blocks, denoting nested loops,
        try statements, and such.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_POP_EXCEPT(self):
        """
        Removes one block from the block stack. The popped block must be an exception handler block, as implicitly
        created when entering an except handler. In addition to popping extraneous values from the frame stack,
        the last three popped values are used to restore the exception state.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_END_FINALLY(self):
        """
        Terminates a finally clause. The interpreter recalls whether the exception has to be re-raised, or whether
        the function returns, and continues with the outer-next block.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_LOAD_BUILD_CLASS(self):
        """
        Pushes builtins.__build_class__() onto the stack. It is later called by CALL_FUNCTION to construct a class.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_SETUP_WITH(self, delta):
        """
        This opcode performs several operations before a with block starts. First, it loads __exit__() from the 
        context manager and pushes it onto the stack for later use by WITH_CLEANUP. Then, __enter__() is called, and
        a finally block pointing to delta is pushed. Finally, the result of calling the enter method is pushed onto the
        stack. The next opcode will either ignore it (POP_TOP), or store it in (a) variable(s) (STORE_FAST, STORE_NAME,
        or UNPACK_SEQUENCE).
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_WITH_CLEANUP(self):
        """
        Cleans up the stack when a with statement block exits. TOS is the context manager’s __exit__() bound method.
        Below TOS are 1–3 values indicating how/why the finally clause was entered:
        SECOND = None
        (SECOND, THIRD) = (WHY_{RETURN,CONTINUE}), retval
        SECOND = WHY_*; no retval below it
        (SECOND, THIRD, FOURTH) = exc_info()
        In the last case, TOS(SECOND, THIRD, FOURTH) is called, otherwise TOS(None, None, None). In addition, TOS is
        removed from the stack.

        If the stack represents an exception, and the function call returns a ‘true’ value, this information is “zapped”
        and replaced with a single WHY_SILENCED to prevent END_FINALLY from re-raising the exception. (But non-local gotos
        will still be resumed.)

        All of the following opcodes expect arguments. An argument is two bytes, with the more significant byte last.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_STORE_NAME(self, namei):
        """
        Implements name = TOS. namei is the index of name in the attribute co_names of the code object. The compiler tries
        to use STORE_FAST or STORE_GLOBAL if possible.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_DELETE_NAME(self, namei):
        """
        Implements del name, where namei is the index into co_names attribute of the code object.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_UNPACK_SEQUENCE(self, count):
        """
        Unpacks TOS into count individual values, which are put onto the stack right-to-left.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_UNPACK_EX(self, counts):
        """
        Implements assignment with a starred target: Unpacks an iterable in TOS into individual values, where the total number
        of values can be smaller than the number of items in the iterable: one the new values will be a list of all leftover items.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    # The low byte of counts is the number of values before the list value, the high byte of counts the number of values after it. The resulting values are put onto the stack right-to-left.

    def execute_STORE_ATTR(self, namei):
        """
        Implements TOS.name = TOS1, where namei is the index of name in co_names.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_DELETE_ATTR(self, namei):
        """
        Implements del TOS.name, using namei as index into co_names.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_STORE_GLOBAL(self, namei):
        """
        Works as STORE_NAME, but stores the name as a global.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_DELETE_GLOBAL(self, namei):
        """
        Works as DELETE_NAME, but deletes a global name.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_LOAD_CONST(self, consti):
        """
        Pushes co_consts[consti] onto the stack.
        """
        self.__stack.append(self.__constants[consti])


    def execute_LOAD_NAME(self, namei):
        """
        Pushes the value associated with co_names[namei] onto the stack.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BUILD_TUPLE(self, count):
        """
        Creates a tuple consuming count items from the stack, and pushes the resulting tuple onto the stack.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BUILD_LIST(self, count):
        """
        Works as BUILD_TUPLE, but creates a list.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BUILD_SET(self, count):
        """
        Works as BUILD_TUPLE, but creates a set.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_BUILD_MAP(self, count):
        """
        Pushes a new dictionary object onto the stack. The dictionary is pre-sized to hold count entries.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_LOAD_ATTR(self, namei):
        """
        Replaces TOS with getattr(TOS, co_names[namei]).
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_COMPARE_OP(self, compare_op):
        """
        Performs a Boolean operation. The operation name can be found in cmp_op[opname].
        """
        w = self.__stack.pop()
        v = self.__stack.pop()
        if len(COMPARE_OPERATORS) < compare_op:
            raise NotImplementedError("Compare Op %s not implemented" % opname)

        value = COMPARE_OPERATORS[compare_op](v, w)
        self.__stack.append(value)

    def execute_IMPORT_NAME(self, namei):
        """
        Imports the module co_names[namei]. TOS and TOS1 are popped and provide the fromlist and level arguments of __import__().
        The module object is pushed onto the stack. The current namespace is not affected: for a proper import statement, a subsequent
        STORE_FAST instruction modifies the namespace.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_IMPORT_FROM(self, namei):
        """
        Loads the attribute co_names[namei] from the module found in TOS. The resulting object is pushed onto the stack,
        to be subsequently stored by a STORE_FAST instruction.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_JUMP_FORWARD(self, delta):
        """
        Increments bytecode counter by delta.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_POP_JUMP_IF_TRUE(self, target):
        """
        If TOS is true, sets the bytecode counter to target. TOS is popped.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_POP_JUMP_IF_FALSE(self, target):
        """
        If TOS is false, sets the bytecode counter to target. TOS is popped.
        """
        if not self.__stack.pop():
            self.__ip = target

    def execute_JUMP_IF_TRUE_OR_POP(self, target):
        """
        If TOS is true, sets the bytecode counter to target and leaves TOS on the stack. Otherwise (TOS is false), TOS is popped.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_JUMP_IF_FALSE_OR_POP(self, target):
        """
        If TOS is false, sets the bytecode counter to target and leaves TOS on the stack. Otherwise (TOS is true), TOS is popped.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_JUMP_ABSOLUTE(self, target):
        """
        Set bytecode counter to target.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_FOR_ITER(self, delta):
        """
        TOS is an iterator. Call its __next__() method. If this yields a new value, push it on the stack (leaving the iterator below it).
        If the iterator indicates it is exhausted TOS is popped, and the byte code counter is incremented by delta.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_LOAD_GLOBAL(self, namei):
        """
        Loads the global named co_names[namei] onto the stack.
        """
        name = self.__names[namei]
        if name in self.__globals_dict:
            self.__stack.append(self.__globals_dict[name])
        else:
            self.__stack.append(self.__builtins_dict[name])

    def execute_SETUP_LOOP(self, delta):
        """
        Pushes a block for a loop onto the block stack. The block spans from the current instruction with a size of delta bytes.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_SETUP_EXCEPT(self, delta):
        """
        Pushes a try block from a try-except clause onto the block stack. delta points to the first except block.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_SETUP_FINALLY(self, delta):
        """
        Pushes a try block from a try-except clause onto the block stack. delta points to the finally block.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_STORE_MAP(self):
        """
        Store a key and value pair in a dictionary. Pops the key and value while leaving the dictionary on the stack.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_LOAD_FAST(self, var_num):
        """
        Pushes a reference to the local co_varnames[var_num] onto the stack.
        """
        self.__stack.append(self.__locals[var_num])


    def execute_STORE_FAST(self, var_num):
        """
        Stores TOS into the local co_varnames[var_num].
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_DELETE_FAST(self, var_num):
        """
        Deletes local co_varnames[var_num].
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_LOAD_CLOSURE(self, i):
        """
        Pushes a reference to the cell contained in slot i of the cell and free variable storage. The name of the variable is
        co_cellvars[i] if i is less than the length of co_cellvars. Otherwise it is co_freevars[i - len(co_cellvars)].
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_LOAD_DEREF(self, i):
        """
        Loads the cell contained in slot i of the cell and free variable storage. Pushes a reference to the object the cell
        contains on the stack.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_LOAD_CLASSDEREF(self, i):
        """
        Much like LOAD_DEREF but first checks the locals dictionary before consulting the cell. This is used for loading free
        variables in class bodies.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_STORE_DEREF(self, i):
        """
        Stores TOS into the cell contained in slot i of the cell and free variable storage.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_DELETE_DEREF(self, i):
        """
        Empties the cell contained in slot i of the cell and free variable storage. Used by the del statement.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_RAISE_VARARGS(self, argc):
        """
        Raises an exception. argc indicates the number of parameters to the raise statement, ranging from 0 to 3. The handler will
        find the traceback as TOS2, the parameter as TOS1, and the exception as TOS.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_CALL_FUNCTION(self, argc):
        """
        Calls a function. The low byte of argc indicates the number of positional parameters, the high byte the number of keyword
        parameters. On the stack, the opcode finds the keyword parameters first. For each keyword argument, the value is on top of
        the key. Below the keyword parameters, the positional parameters are on the stack, with the right-most parameter on top. 
        Below the parameters, the function object to call is on the stack. Pops all function arguments, and the function itself off
        the stack, and pushes the return value.
        """
        assert argc < 255, "can't handle keyword arguments"
        args = [self.__stack.pop() for i in range(argc)]
        callable = self.__stack.pop()
        vm = BytecodeVM(callable, *args)
        vm.execute()
        value = vm.value
        self.__stack.append(value)

    def execute_MAKE_FUNCTION(self, argc):
        """
        Pushes a new function object on the stack. From bottom to top, the consumed stack must consist of argc & 0xFF default argument
        objects in positional order (argc >> 8) & 0xFF pairs of name and default argument, with the name just below the object on the
        stack, for keyword-only parameters (argc >> 16) & 0x7FFF parameter annotation objects a tuple listing the parameter names for the
        annotations (only if there are ony annotation objects) the code associated with the function (at TOS1) the qualified name of the
        function (at TOS)
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_MAKE_CLOSURE(self, argc):
        """
        Creates a new function object, sets its __closure__ slot, and pushes it on the stack. TOS is the qualified name of the function,
        TOS1 is the code associated with the function, and TOS2 is the tuple containing cells for the closure’s free variables. argc is
        interpreted as in MAKE_FUNCTION; the annotations and defaults are also in the same order below TOS2.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)

    def execute_BUILD_SLICE(self, argc):
        """
        Pushes a slice object on the stack. argc must be 2 or 3. If it is 2, slice(TOS1, TOS) is pushed; if it is 3, slice(TOS2, TOS1, TOS)
        is pushed. See the slice() built-in function for more information.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_EXTENDED_ARG(self, ext):
        """
        Prefixes any opcode which has an argument too big to fit into the default two bytes. ext holds two additional bytes which, taken
        together with the subsequent opcode’s argument, comprise a four-byte argument, ext being the two most-significant bytes.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_CALL_FUNCTION_VAR(self, argc):
        """
        Calls a function. argc is interpreted as in CALL_FUNCTION. The top element on the stack contains the variable argument list,
        followed by keyword and positional arguments.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_CALL_FUNCTION_KW(self, argc):
        """
        Calls a function. argc is interpreted as in CALL_FUNCTION. The top element on the stack contains the keyword arguments dictionary,
        followed by explicit keyword and positional arguments.
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)


    def execute_CALL_FUNCTION_VAR_KW(self, argc):
        """
        Calls a function. argc is interpreted as in CALL_FUNCTION. The top element on the stack contains the keyword arguments dictionary,
        followed by the variable-arguments tuple, followed by explicit keyword and positional arguments.            
        """
        raise NotImplementedError("Method %s not implemented" % sys._getframe().f_code.co_name)
