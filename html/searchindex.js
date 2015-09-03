Search.setIndex({envversion:47,filenames:["index","ir","main","optimizer","pyjit","utils","vm"],objects:{"":{ir:[1,0,0,"-"],main:[2,0,0,"-"],optimizer:[3,0,0,"-"],pyjit:[4,0,0,"-"],utils:[5,0,0,"-"],vm:[6,0,0,"-"]},"ir.base_ir_visitor":{IRBaseVisitor:[1,3,1,""]},"ir.base_ir_visitor.IRBaseVisitor":{visit_addinstruction:[1,1,1,""],visit_allocainstruction:[1,1,1,""],visit_andinstruction:[1,1,1,""],visit_arithmeticshiftrightinstruction:[1,1,1,""],visit_basicblock:[1,1,1,""],visit_callinstruction:[1,1,1,""],visit_castinstruction:[1,1,1,""],visit_conditionalbranchinstruction:[1,1,1,""],visit_divinstruction:[1,1,1,""],visit_extractelementinstruction:[1,1,1,""],visit_faddinstruction:[1,1,1,""],visit_fcmpinstruction:[1,1,1,""],visit_fdivinstruction:[1,1,1,""],visit_fmulinstruction:[1,1,1,""],visit_fsubinstruction:[1,1,1,""],visit_function:[1,1,1,""],visit_gepinstruction:[1,1,1,""],visit_icmpinstruction:[1,1,1,""],visit_indirectbranchinstruction:[1,1,1,""],visit_insertelementinstruction:[1,1,1,""],visit_loadinstruction:[1,1,1,""],visit_logicalshiftrightinstruction:[1,1,1,""],visit_module:[1,1,1,""],visit_mulinstruction:[1,1,1,""],visit_orinstruction:[1,1,1,""],visit_phiinstruction:[1,1,1,""],visit_returninstruction:[1,1,1,""],visit_selectinstruction:[1,1,1,""],visit_shiftleftinstruction:[1,1,1,""],visit_storeinstruction:[1,1,1,""],visit_subinstruction:[1,1,1,""],visit_switchinstruction:[1,1,1,""],visit_terminateinstruction:[1,1,1,""],visit_xorinstruction:[1,1,1,""]},"ir.codegen":{Emit:[1,3,1,""]},"ir.codegen.Emit":{visit_function:[1,1,1,""],visit_module:[1,1,1,""]},"ir.constants":{Constant:[1,3,1,""],DoubleConstant:[1,3,1,""],FloatConstant:[1,3,1,""],IntConstant:[1,3,1,""],StrConstant:[1,3,1,""]},"ir.constants.DoubleConstant":{initializer:[1,2,1,""],name:[1,2,1,""],type:[1,2,1,""]},"ir.constants.FloatConstant":{initializer:[1,2,1,""],name:[1,2,1,""],type:[1,2,1,""]},"ir.constants.IntConstant":{initializer:[1,2,1,""],name:[1,2,1,""],type:[1,2,1,""]},"ir.constants.StrConstant":{initializer:[1,2,1,""],name:[1,2,1,""],type:[1,2,1,""]},"ir.context":{Context:[1,3,1,""]},"ir.exceptions":{IllegalArgumentException:[1,4,1,""],InvalidInsertionPointException:[1,4,1,""],InvalidInstructionException:[1,4,1,""],InvalidTypeException:[1,4,1,""],InvalidUsageModel:[1,4,1,""],NoBBTerminatorException:[1,4,1,""]},"ir.function":{Function:[1,3,1,""],Global:[1,3,1,""],NameGenerator:[1,3,1,""]},"ir.function.Function":{args:[1,2,1,""],basic_blocks:[1,2,1,""],name:[1,2,1,""],name_generator:[1,2,1,""],render_signature:[1,1,1,""],type:[1,2,1,""],validate:[1,1,1,""],verify_args:[1,1,1,""]},"ir.function.Global":{initializer:[1,2,1,""],name:[1,2,1,""],type:[1,2,1,""]},"ir.function.NameGenerator":{generate:[1,1,1,""]},"ir.instructions":{AddInstruction:[1,3,1,""],AllocaInstruction:[1,3,1,""],AndInstruction:[1,3,1,""],ArithmeticShiftRightInstruction:[1,3,1,""],BasicBlock:[1,3,1,""],BinOpInstruction:[1,3,1,""],BitwiseBinaryInstruction:[1,3,1,""],BranchInstruction:[1,3,1,""],CallInstruction:[1,3,1,""],CastInstruction:[1,3,1,""],CompareInstruction:[1,3,1,""],CompareTypes:[1,3,1,""],ConditionalBranchInstruction:[1,3,1,""],DivInstruction:[1,3,1,""],ExtractElementInstruction:[1,3,1,""],FAddInstruction:[1,3,1,""],FBinOpInstruction:[1,3,1,""],FCmpInstruction:[1,3,1,""],FDivInstruction:[1,3,1,""],FMulInstruction:[1,3,1,""],FSubInstruction:[1,3,1,""],GEPInstruction:[1,3,1,""],ICmpInstruction:[1,3,1,""],IndirectBranchInstruction:[1,3,1,""],InsertElementInstruction:[1,3,1,""],Instruction:[1,3,1,""],InstructionList:[1,3,1,""],LoadInstruction:[1,3,1,""],LogicalShiftRightInstruction:[1,3,1,""],MulInstruction:[1,3,1,""],OrInstruction:[1,3,1,""],PhiInstruction:[1,3,1,""],ReturnInstruction:[1,3,1,""],SelectInstruction:[1,3,1,""],ShiftLeftInstruction:[1,3,1,""],StoreInstruction:[1,3,1,""],SubInstruction:[1,3,1,""],SwitchInstruction:[1,3,1,""],TerminateInstruction:[1,3,1,""],XorInstruction:[1,3,1,""]},"ir.instructions.BasicBlock":{find_instruction_idx:[1,1,1,""],instructions:[1,2,1,""],name:[1,2,1,""],parent:[1,2,1,""],validate:[1,1,1,""]},"ir.instructions.BinOpInstruction":{OP_ADD:[1,2,1,""],OP_DIV:[1,2,1,""],OP_MUL:[1,2,1,""],OP_SUB:[1,2,1,""],lhs:[1,2,1,""],operator:[1,2,1,""],rhs:[1,2,1,""],type:[1,2,1,""]},"ir.instructions.BitwiseBinaryInstruction":{op1:[1,2,1,""],op2:[1,2,1,""]},"ir.instructions.CallInstruction":{"function":[1,2,1,""],args:[1,2,1,""],type:[1,2,1,""]},"ir.instructions.CompareInstruction":{condition:[1,2,1,""],op1:[1,2,1,""],op2:[1,2,1,""]},"ir.instructions.CompareTypes":{EQ:[1,2,1,""],NE:[1,2,1,""],SGE:[1,2,1,""],SGT:[1,2,1,""],SLE:[1,2,1,""],SLT:[1,2,1,""],UGE:[1,2,1,""],UGT:[1,2,1,""],ULE:[1,2,1,""],ULT:[1,2,1,""],get_str:[1,6,1,""]},"ir.instructions.ConditionalBranchInstruction":{bb_false:[1,2,1,""],bb_true:[1,2,1,""],cmp_inst:[1,2,1,""],cmp_value:[1,2,1,""]},"ir.instructions.FBinOpInstruction":{OP_ADD:[1,2,1,""],OP_DIV:[1,2,1,""],OP_MUL:[1,2,1,""],OP_SUB:[1,2,1,""],lhs:[1,2,1,""],operator:[1,2,1,""],rhs:[1,2,1,""]},"ir.instructions.Instruction":{inst_idx:[1,2,1,""],name:[1,2,1,""],needs_name:[1,2,1,""],operands:[1,2,1,""],parent:[1,2,1,""]},"ir.instructions.InstructionList":{append:[1,1,1,""],insert:[1,1,1,""]},"ir.instructions.ReturnInstruction":{value:[1,2,1,""]},"ir.interpreter":{Frame:[1,3,1,""],IRVirtualMachine:[1,3,1,""]},"ir.interpreter.Frame":{add_to_frame:[1,1,1,""],get_symbol:[1,1,1,""],name:[1,2,1,""]},"ir.interpreter.IRVirtualMachine":{eval_result:[1,2,1,""],visit_addinstruction:[1,1,1,""],visit_allocainstruction:[1,1,1,""],visit_andinstruction:[1,1,1,""],visit_arithmeticshiftrightinstruction:[1,1,1,""],visit_basicblock:[1,1,1,""],visit_binop:[1,1,1,""],visit_callinstruction:[1,1,1,""],visit_castinstruction:[1,1,1,""],visit_conditionalbranchinstruction:[1,1,1,""],visit_divinstruction:[1,1,1,""],visit_extractelementinstruction:[1,1,1,""],visit_faddinstruction:[1,1,1,""],visit_fcmpinstruction:[1,1,1,""],visit_fdivinstruction:[1,1,1,""],visit_fmulinstruction:[1,1,1,""],visit_fsubinstruction:[1,1,1,""],visit_function:[1,1,1,""],visit_gepinstruction:[1,1,1,""],visit_icmpinstruction:[1,1,1,""],visit_indirectbranchinstruction:[1,1,1,""],visit_insertelementinstruction:[1,1,1,""],visit_loadinstruction:[1,1,1,""],visit_logicalshiftrightinstruction:[1,1,1,""],visit_module:[1,1,1,""],visit_mulinstruction:[1,1,1,""],visit_orinstruction:[1,1,1,""],visit_phiinstruction:[1,1,1,""],visit_returninstruction:[1,1,1,""],visit_selectinstruction:[1,1,1,""],visit_shiftleftinstruction:[1,1,1,""],visit_storeinstruction:[1,1,1,""],visit_subinstruction:[1,1,1,""],visit_switchinstruction:[1,1,1,""],visit_terminateinstruction:[1,1,1,""],visit_xorinstruction:[1,1,1,""]},"ir.irbuilder":{IRBuilder:[1,3,1,""]},"ir.irbuilder.IRBuilder":{context:[1,2,1,""],create_add:[1,1,1,""],create_basic_block:[1,1,1,""],create_branch:[1,1,1,""],create_call:[1,1,1,""],create_cond_branch:[1,1,1,""],create_div:[1,1,1,""],create_fadd:[1,1,1,""],create_fdiv:[1,1,1,""],create_fmul:[1,1,1,""],create_fsub:[1,1,1,""],create_function:[1,1,1,""],create_function_type:[1,1,1,""],create_global:[1,1,1,""],create_icmp:[1,1,1,""],create_mul:[1,1,1,""],create_return:[1,1,1,""],create_sub:[1,1,1,""],insert_after:[1,1,1,""],insert_before:[1,1,1,""],module:[1,2,1,""],set_entry_point:[1,1,1,""]},"ir.module":{Module:[1,3,1,""]},"ir.module.Module":{add_global:[1,1,1,""],context:[1,2,1,""],datalayout:[1,2,1,""],entry_point:[1,2,1,""],function_decls:[1,2,1,""],functions:[1,2,1,""],globals:[1,2,1,""],name:[1,2,1,""],target_arch:[1,2,1,""],validate:[1,1,1,""]},"ir.types":{BaseType:[1,3,1,""],BitType:[1,3,1,""],BoolType:[1,3,1,""],ByteType:[1,3,1,""],DoubleType:[1,3,1,""],FloatType:[1,3,1,""],FunctionType:[1,3,1,""],IntType:[1,3,1,""],PointerType:[1,3,1,""]},"ir.types.FunctionType":{arg_types:[1,2,1,""],ret_type:[1,2,1,""]},"ir.types.IntType":{bits:[1,2,1,""]},"ir.utils":{is_terminator_instruction:[1,5,1,""],render_list_with_parens:[1,5,1,""]},"ir.validator":{Validator:[1,3,1,""],verify:[1,5,1,""]},"ir.validator.Validator":{validate:[1,1,1,""]},"ir.value":{Argument:[1,3,1,""],Value:[1,3,1,""]},"ir.value.Argument":{name:[1,2,1,""],type:[1,2,1,""]},"optimizer.basicpass":{PrintBasicBlocksPass:[3,3,1,""],PrintFunctionsPass:[3,3,1,""]},"optimizer.basicpass.PrintBasicBlocksPass":{run_on_function:[3,1,1,""]},"optimizer.basicpass.PrintFunctionsPass":{run_on_module:[3,1,1,""]},"optimizer.pass_support":{FunctionPass:[3,3,1,""],InstVisitorPass:[3,3,1,""],ModulePass:[3,3,1,""]},"optimizer.pass_support.FunctionPass":{run_on_function:[3,1,1,""]},"optimizer.pass_support.InstVisitorPass":{generic_visit:[3,1,1,""],visit:[3,1,1,""],visit_addinstruction:[3,1,1,""],visit_allocainstruction:[3,1,1,""],visit_andinstruction:[3,1,1,""],visit_arithmeticshiftrightinstruction:[3,1,1,""],visit_basicblock:[3,1,1,""],visit_branchinstruction:[3,1,1,""],visit_callinstruction:[3,1,1,""],visit_castinstruction:[3,1,1,""],visit_conditionalbranchinstruction:[3,1,1,""],visit_divinstruction:[3,1,1,""],visit_extractelementinstruction:[3,1,1,""],visit_faddinstruction:[3,1,1,""],visit_fcmpinstruction:[3,1,1,""],visit_fdivinstruction:[3,1,1,""],visit_fmulinstruction:[3,1,1,""],visit_fsubinstruction:[3,1,1,""],visit_function:[3,1,1,""],visit_gepinstruction:[3,1,1,""],visit_icmpinstruction:[3,1,1,""],visit_indirectbranchinstruction:[3,1,1,""],visit_insertelementinstruction:[3,1,1,""],visit_loadinstruction:[3,1,1,""],visit_logicalshiftrightinstruction:[3,1,1,""],visit_module:[3,1,1,""],visit_mulinstruction:[3,1,1,""],visit_orinstruction:[3,1,1,""],visit_phiinstruction:[3,1,1,""],visit_returninstruction:[3,1,1,""],visit_selectinstruction:[3,1,1,""],visit_shiftleftinstruction:[3,1,1,""],visit_storeinstruction:[3,1,1,""],visit_subinstruction:[3,1,1,""],visit_switchinstruction:[3,1,1,""],visit_terminateinstruction:[3,1,1,""],visit_xorinstruction:[3,1,1,""]},"optimizer.pass_support.ModulePass":{run_on_module:[3,1,1,""]},"optimizer.passmanager":{PassManager:[3,3,1,""]},"optimizer.passmanager.PassManager":{add_function_pass:[3,1,1,""],add_module_pass:[3,1,1,""],run:[3,1,1,""]},"pyjit.codegen":{IREmitter:[4,3,1,""]},"pyjit.codegen.IREmitter":{irbuilder:[4,2,1,""],module:[4,2,1,""],visit_func:[4,1,1,""]},"pyjit.decorators":{arg_pytype:[4,5,1,""],autojit:[4,5,1,""],codegen:[4,5,1,""],specialize:[4,5,1,""],typeinfer:[4,5,1,""]},"pyjit.nodes":{App:[4,3,1,""],AppTy:[4,3,1,""],Assign:[4,3,1,""],BoolTy:[4,3,1,""],Compare:[4,3,1,""],CompareOps:[4,3,1,""],ConstructorTy:[4,3,1,""],DictTy:[4,3,1,""],FloatTy:[4,3,1,""],Func:[4,3,1,""],FuncTy:[4,3,1,""],If:[4,3,1,""],Index:[4,3,1,""],IntTy:[4,3,1,""],ListTy:[4,3,1,""],LitBool:[4,3,1,""],LitFloat:[4,3,1,""],LitInt:[4,3,1,""],LitString:[4,3,1,""],Loop:[4,3,1,""],Noop:[4,3,1,""],Prim:[4,3,1,""],Return:[4,3,1,""],StringTy:[4,3,1,""],TupleTy:[4,3,1,""],Var:[4,3,1,""],VarTy:[4,3,1,""],array:[4,5,1,""],ftv:[4,5,1,""],is_array:[4,5,1,""]},"pyjit.nodes.CompareOps":{LT:[4,2,1,""]},"pyjit.pretty_print":{ast2tree:[4,5,1,""],pformat_ast:[4,5,1,""]},"pyjit.type_infer":{InferError:[4,4,1,""],InferType:[4,3,1,""],TypeSolver:[4,3,1,""],UnderDeteremined:[4,4,1,""],apply:[4,5,1,""],applyList:[4,5,1,""],bind:[4,5,1,""],compose:[4,5,1,""],empty:[4,5,1,""],naming:[4,5,1,""],occurs_check:[4,5,1,""],solve:[4,5,1,""],unify:[4,5,1,""],union:[4,5,1,""]},"pyjit.type_infer.InferType":{fresh:[4,1,1,""],generic_visit:[4,1,1,""],visit:[4,1,1,""],visit_Assign:[4,1,1,""],visit_Func:[4,1,1,""],visit_Index:[4,1,1,""],visit_LitBool:[4,1,1,""],visit_LitFloat:[4,1,1,""],visit_LitInt:[4,1,1,""],visit_LitString:[4,1,1,""],visit_Loop:[4,1,1,""],visit_Noop:[4,1,1,""],visit_Prim:[4,1,1,""],visit_Return:[4,1,1,""],visit_Var:[4,1,1,""]},"pyjit.type_infer.TypeSolver":{solve:[4,6,1,""]},"pyjit.visitors":{PythonVisitor:[4,3,1,""]},"pyjit.visitors.PythonVisitor":{generic_visit:[4,1,1,""],visit_Assign:[4,1,1,""],visit_Attribute:[4,1,1,""],visit_AugAssign:[4,1,1,""],visit_BinOp:[4,1,1,""],visit_Bool:[4,1,1,""],visit_Call:[4,1,1,""],visit_Compare:[4,1,1,""],visit_For:[4,1,1,""],visit_FunctionDef:[4,1,1,""],visit_If:[4,1,1,""],visit_Lambda:[4,1,1,""],visit_List:[4,1,1,""],visit_Module:[4,1,1,""],visit_Name:[4,1,1,""],visit_Num:[4,1,1,""],visit_Pass:[4,1,1,""],visit_Return:[4,1,1,""],visit_Str:[4,1,1,""],visit_Subscript:[4,1,1,""],visit_arg:[4,1,1,""]},"utils.base_visitor":{BaseVisitor:[5,3,1,""]},"utils.base_visitor.BaseVisitor":{generic_visit:[5,1,1,""],visit:[5,1,1,""]},"vm.vm":{BytecodeVM:[6,3,1,""]},"vm.vm.BytecodeVM":{execute:[6,1,1,""],execute_BINARY_ADD:[6,1,1,""],execute_BINARY_AND:[6,1,1,""],execute_BINARY_FLOOR_DIVIDE:[6,1,1,""],execute_BINARY_LSHIFT:[6,1,1,""],execute_BINARY_MODULO:[6,1,1,""],execute_BINARY_MULTIPLY:[6,1,1,""],execute_BINARY_OR:[6,1,1,""],execute_BINARY_POWER:[6,1,1,""],execute_BINARY_RSHIFT:[6,1,1,""],execute_BINARY_SUBSCR:[6,1,1,""],execute_BINARY_SUBTRACT:[6,1,1,""],execute_BINARY_TRUE_DIVIDE:[6,1,1,""],execute_BINARY_XOR:[6,1,1,""],execute_BREAK_LOOP:[6,1,1,""],execute_BUILD_LIST:[6,1,1,""],execute_BUILD_MAP:[6,1,1,""],execute_BUILD_SET:[6,1,1,""],execute_BUILD_SLICE:[6,1,1,""],execute_BUILD_TUPLE:[6,1,1,""],execute_CALL_FUNCTION:[6,1,1,""],execute_CALL_FUNCTION_KW:[6,1,1,""],execute_CALL_FUNCTION_VAR:[6,1,1,""],execute_CALL_FUNCTION_VAR_KW:[6,1,1,""],execute_COMPARE_OP:[6,1,1,""],execute_CONTINUE_LOOP:[6,1,1,""],execute_DELETE_ATTR:[6,1,1,""],execute_DELETE_DEREF:[6,1,1,""],execute_DELETE_FAST:[6,1,1,""],execute_DELETE_GLOBAL:[6,1,1,""],execute_DELETE_NAME:[6,1,1,""],execute_DELETE_SUBSCR:[6,1,1,""],execute_DUP_TOP:[6,1,1,""],execute_DUP_TOP_TWO:[6,1,1,""],execute_END_FINALLY:[6,1,1,""],execute_EXTENDED_ARG:[6,1,1,""],execute_FOR_ITER:[6,1,1,""],execute_GET_ITER:[6,1,1,""],execute_IMPORT_FROM:[6,1,1,""],execute_IMPORT_NAME:[6,1,1,""],execute_IMPORT_STAR:[6,1,1,""],execute_INPLACE_ADD:[6,1,1,""],execute_INPLACE_AND:[6,1,1,""],execute_INPLACE_FLOOR_DIVIDE:[6,1,1,""],execute_INPLACE_LSHIFT:[6,1,1,""],execute_INPLACE_MODULO:[6,1,1,""],execute_INPLACE_MULTIPLY:[6,1,1,""],execute_INPLACE_OR:[6,1,1,""],execute_INPLACE_POWER:[6,1,1,""],execute_INPLACE_RSHIFT:[6,1,1,""],execute_INPLACE_SUBTRACT:[6,1,1,""],execute_INPLACE_TRUE_DIVIDE:[6,1,1,""],execute_INPLACE_XOR:[6,1,1,""],execute_JUMP_ABSOLUTE:[6,1,1,""],execute_JUMP_FORWARD:[6,1,1,""],execute_JUMP_IF_FALSE_OR_POP:[6,1,1,""],execute_JUMP_IF_TRUE_OR_POP:[6,1,1,""],execute_LIST_APPEND:[6,1,1,""],execute_LOAD_ATTR:[6,1,1,""],execute_LOAD_BUILD_CLASS:[6,1,1,""],execute_LOAD_CLASSDEREF:[6,1,1,""],execute_LOAD_CLOSURE:[6,1,1,""],execute_LOAD_CONST:[6,1,1,""],execute_LOAD_DEREF:[6,1,1,""],execute_LOAD_FAST:[6,1,1,""],execute_LOAD_GLOBAL:[6,1,1,""],execute_LOAD_NAME:[6,1,1,""],execute_MAKE_CLOSURE:[6,1,1,""],execute_MAKE_FUNCTION:[6,1,1,""],execute_MAP_ADD:[6,1,1,""],execute_NOP:[6,1,1,""],execute_POP_BLOCK:[6,1,1,""],execute_POP_EXCEPT:[6,1,1,""],execute_POP_JUMP_IF_FALSE:[6,1,1,""],execute_POP_JUMP_IF_TRUE:[6,1,1,""],execute_POP_TOP:[6,1,1,""],execute_PRINT_EXPR:[6,1,1,""],execute_RAISE_VARARGS:[6,1,1,""],execute_RETURN_VALUE:[6,1,1,""],execute_ROT_THREE:[6,1,1,""],execute_ROT_TWO:[6,1,1,""],execute_SETUP_EXCEPT:[6,1,1,""],execute_SETUP_FINALLY:[6,1,1,""],execute_SETUP_LOOP:[6,1,1,""],execute_SETUP_WITH:[6,1,1,""],execute_SET_ADD:[6,1,1,""],execute_STORE_ATTR:[6,1,1,""],execute_STORE_DEREF:[6,1,1,""],execute_STORE_FAST:[6,1,1,""],execute_STORE_GLOBAL:[6,1,1,""],execute_STORE_MAP:[6,1,1,""],execute_STORE_NAME:[6,1,1,""],execute_STORE_SUBSCR:[6,1,1,""],execute_UNARY_INVERT:[6,1,1,""],execute_UNARY_NEGATIVE:[6,1,1,""],execute_UNARY_NOT:[6,1,1,""],execute_UNARY_POSITIVE:[6,1,1,""],execute_UNPACK_EX:[6,1,1,""],execute_UNPACK_SEQUENCE:[6,1,1,""],execute_WITH_CLEANUP:[6,1,1,""],execute_YIELD_FROM:[6,1,1,""],execute_YIELD_VALUE:[6,1,1,""],print_members:[6,1,1,""],value:[6,2,1,""]},ir:{"function":[1,0,0,"-"],base_ir_visitor:[1,0,0,"-"],codegen:[1,0,0,"-"],constants:[1,0,0,"-"],context:[1,0,0,"-"],exceptions:[1,0,0,"-"],instructions:[1,0,0,"-"],interpreter:[1,0,0,"-"],irbuilder:[1,0,0,"-"],module:[1,0,0,"-"],types:[1,0,0,"-"],utils:[1,0,0,"-"],validator:[1,0,0,"-"],value:[1,0,0,"-"]},main:{generate_ir:[2,5,1,""],test_bytecode_vm:[2,5,1,""]},optimizer:{basicpass:[3,0,0,"-"],pass_support:[3,0,0,"-"],passmanager:[3,0,0,"-"]},pyjit:{codegen:[4,0,0,"-"],decorators:[4,0,0,"-"],nodes:[4,0,0,"-"],pretty_print:[4,0,0,"-"],type_infer:[4,0,0,"-"],visitors:[4,0,0,"-"]},utils:{base_visitor:[5,0,0,"-"]},vm:{vm:[6,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","method","Python method"],"2":["py","attribute","Python attribute"],"3":["py","class","Python class"],"4":["py","exception","Python exception"],"5":["py","function","Python function"],"6":["py","staticmethod","Python static method"]},objtypes:{"0":"py:module","1":"py:method","2":"py:attribute","3":"py:class","4":"py:exception","5":"py:function","6":"py:staticmethod"},terms:{"0x7fff":6,"0xff":6,"__build_class__":6,"__closure__":6,"__enter__":6,"__exit__":6,"__import__":6,"__next__":6,"_ast":4,"boolean":6,"break":6,"byte":6,"case":6,"class":[1,3,4,5,6],"default":6,"final":6,"function":[],"goto":6,"import":6,"new":6,"return":[4,6],"static":[1,4],"true":[1,4,6],"try":6,"var":4,"while":6,add:6,add_function_pass:3,add_glob:1,add_module_pass:3,add_to_fram:1,addinstruct:1,addit:6,address:6,address_spac:1,affect:6,after:6,all:[1,6],allocainstruct:1,also:6,andinstruct:1,ani:6,annot:6,app:4,append:[1,6],appli:4,applylist:4,appti:4,arg:[1,3,4,5,6],arg_list:1,arg_pytyp:4,arg_ti:1,arg_typ:1,argc:6,argsti:4,argti:4,argument:[1,6],arithmeticshiftrightinstruct:1,arrai:4,assign:[4,6],associ:6,ast2tre:4,ast:4,attribut:6,autojit:4,base:[1,3,4,5,6],base_ir_visitor:[],base_typ:1,base_visitor:[],basetyp:1,basevisitor:[1,4,5],basic_block:1,basicblock:1,basicpass:[],bb_fals:1,bb_true:1,befor:6,begin:4,below:6,big:6,bind:4,binop:1,binopinstruct:1,bit:1,bitsiz:1,bittyp:1,bitwisebinaryinstruct:1,block:6,bodi:[4,6],boolti:4,booltyp:1,bottom:6,bound:6,branchinstruct:1,build_tupl:6,builder:1,built:[1,6],builtin:6,bytecod:6,bytecodevm:6,bytetyp:1,call:6,call_funct:6,caller:6,callinstruct:1,can:6,castinstruct:1,cell:6,check:6,claus:6,clean:6,closur:6,cmp_inst:1,cmp_op:6,cmp_valu:1,co_cellvar:6,co_const:6,co_freevar:6,co_nam:6,co_varnam:6,code:6,codegen:[],compar:4,compare_op:6,compareinstruct:1,compareop:4,compareti:1,comparetyp:1,compil:6,compos:4,comprehens:6,compris:6,cond:1,condit:1,conditionalbranchinstruct:1,consist:6,constant:[],consti:6,construct:6,constructorti:4,consult:6,consum:6,contain:6,content:[],context:[],continu:6,count:6,counter:6,creat:[1,6],create_add:1,create_basic_block:1,create_branch:1,create_cal:1,create_cond_branch:1,create_div:1,create_fadd:1,create_fdiv:1,create_fmul:1,create_fsub:1,create_funct:1,create_function_typ:1,create_glob:1,create_icmp:1,create_mul:1,create_return:1,create_sub:1,current:6,current_modul:1,custom_list:1,datalayout:1,decor:[],del:6,deleg:6,delet:6,delete_nam:6,delta:6,denot:6,dict:6,dictionari:6,dictti:4,directli:6,divinstruct:1,doubleconst:1,doubletyp:1,down:6,due:6,duplic:6,each:6,either:6,element:6,emit:1,empti:[4,6],end:4,end_fin:6,enter:6,entri:6,entry_point:1,eval_result:1,exc_info:6,except:[],execut:6,execute_binary_add:6,execute_binary_and:6,execute_binary_floor_divid:6,execute_binary_lshift:6,execute_binary_modulo:6,execute_binary_multipli:6,execute_binary_or:6,execute_binary_pow:6,execute_binary_rshift:6,execute_binary_subscr:6,execute_binary_subtract:6,execute_binary_true_divid:6,execute_binary_xor:6,execute_break_loop:6,execute_build_list:6,execute_build_map:6,execute_build_set:6,execute_build_slic:6,execute_build_tupl:6,execute_call_funct:6,execute_call_function_kw:6,execute_call_function_var:6,execute_call_function_var_kw:6,execute_compare_op:6,execute_continue_loop:6,execute_delete_attr:6,execute_delete_deref:6,execute_delete_fast:6,execute_delete_glob:6,execute_delete_nam:6,execute_delete_subscr:6,execute_dup_top:6,execute_dup_top_two:6,execute_end_fin:6,execute_extended_arg:6,execute_for_it:6,execute_get_it:6,execute_import_from:6,execute_import_nam:6,execute_import_star:6,execute_inplace_add:6,execute_inplace_and:6,execute_inplace_floor_divid:6,execute_inplace_lshift:6,execute_inplace_modulo:6,execute_inplace_multipli:6,execute_inplace_or:6,execute_inplace_pow:6,execute_inplace_rshift:6,execute_inplace_subtract:6,execute_inplace_true_divid:6,execute_inplace_xor:6,execute_jump_absolut:6,execute_jump_forward:6,execute_jump_if_false_or_pop:6,execute_jump_if_true_or_pop:6,execute_list_append:6,execute_load_attr:6,execute_load_build_class:6,execute_load_classderef:6,execute_load_closur:6,execute_load_const:6,execute_load_deref:6,execute_load_fast:6,execute_load_glob:6,execute_load_nam:6,execute_make_closur:6,execute_make_funct:6,execute_map_add:6,execute_nop:6,execute_pop_block:6,execute_pop_except:6,execute_pop_jump_if_fals:6,execute_pop_jump_if_tru:6,execute_pop_top:6,execute_print_expr:6,execute_raise_vararg:6,execute_return_valu:6,execute_rot_thre:6,execute_rot_two:6,execute_set_add:6,execute_setup_except:6,execute_setup_fin:6,execute_setup_loop:6,execute_setup_with:6,execute_store_attr:6,execute_store_deref:6,execute_store_fast:6,execute_store_glob:6,execute_store_map:6,execute_store_nam:6,execute_store_subscr:6,execute_unary_invert:6,execute_unary_neg:6,execute_unary_not:6,execute_unary_posit:6,execute_unpack_ex:6,execute_unpack_sequ:6,execute_with_cleanup:6,execute_yield_from:6,execute_yield_valu:6,exhaust:6,exit:6,expect:6,explicit:6,express:6,ext:6,extractelementinstruct:1,extran:6,faddinstruct:1,fals:[4,6],fbinopinstruct:1,fcmpinstruct:1,fdivinstruct:1,find:6,find_instruction_idx:1,first:6,fit:6,floatconst:1,floatti:4,floattyp:1,fmulinstruct:1,fname:4,follow:6,for_it:6,found:6,four:6,fourth:6,frame:[1,6],free:6,fresh:4,from:6,fromlist:6,fsubinstruct:1,ftv:4,func:[1,4],functi:4,function_decl:1,functionpass:3,functiontyp:1,gener:[1,6],generate_ir:2,generic_visit:[3,4,5],gepinstruct:1,get_str:1,get_symbol:1,getattr:6,global:[1,6],globalv:1,handler:6,have:1,high:6,hold:[1,6],how:6,icmpinstruct:1,idx:1,ignor:6,illegalargumentexcept:1,implement:6,implicitli:6,include_attr:4,increment:6,index:[0,4,6],indirectbranchinstruct:1,individu:6,infer_ti:4,infererror:4,infertyp:4,inform:[1,6],initi:1,insert:1,insert_aft:1,insert_befor:1,insertelementinstruct:1,inst:1,inst_idx:1,instruct:[],instructionlist:1,instvisitorpass:3,intconst:1,interact:6,interpret:[],intti:4,inttyp:1,invalidinsertionpointexcept:1,invalidinstructionexcept:1,invalidtypeexcept:1,invalidusagemodel:1,irbasevisitor:1,irbuild:[],iremitt:4,irvirtualmachin:1,is_arrai:4,is_terminator_instruct:1,item:6,iter:6,itself:6,jit:1,jump:6,just:6,kei:6,keyword:6,kwarg:[1,3],last:6,later:6,leav:6,left:6,leftov:6,len:6,length:6,less:6,level:6,lift:6,like:6,list:[1,6],listti:4,litbool:4,litfloat:4,litint:4,litstr:4,load:6,load_deref:6,loadinstruct:1,local:6,logicalshiftrightinstruct:1,loop:[4,6],low:6,main:[],make_funct:6,manag:6,method:6,mgu:4,mod_nam:4,mode:6,modifi:[1,6],modul:[],modulepass:3,more:6,most:6,move:6,much:6,mulinstruct:1,must:6,name:[1,4,6],name_gener:1,namegener:1,namei:6,namespac:6,need:1,needs_nam:1,nest:6,next:6,nobbterminatorexcept:1,node:[],nodevisitor:4,non:6,none:[1,4,6],noop:4,noth:6,number:6,object:[1,3,4,5,6],occurs_check:4,off:6,oni:6,onli:6,onto:6,op1:1,op2:1,op_add:1,op_div:1,op_mul:1,op_sub:1,oparg:6,opcod:6,oper:[1,6],operand:1,opnam:6,optim:[],option:1,order:6,orinstruct:1,other:1,otherwis:6,outer:6,packag:[],page:0,pair:6,paramet:6,parent:1,pass_support:[],passmanag:[],per:6,perform:6,pformat_ast:4,phiinstruct:1,place:6,placehold:6,point:6,pointertyp:1,pop:6,pop_top:6,posit:6,possibl:6,pre:6,prefix:6,pretty_print:[],prevent:6,prim:4,print:6,print_memb:6,printbasicblockspass:3,printfunctionspass:3,proper:6,provid:6,push:6,put:6,pyjit:[],pythonvisitor:4,qualifi:6,rais:6,rang:6,recal:6,ref:4,refer:6,remov:6,render_list_with_paren:1,render_signatur:1,replac:6,repres:6,restor:6,result:6,resum:6,ret_ti:1,ret_typ:1,retti:4,returninstruct:1,retval:6,right:6,run:3,run_on_funct:3,run_on_modul:3,same:6,search:0,second:6,see:6,selectinstruct:1,set:6,set_entry_point:1,setitem:6,sever:6,sge:1,sgt:1,shiftleftinstruct:1,should:6,signific:6,singl:6,size:6,sle:1,slice:6,slot:6,slt:1,smaller:6,solv:4,sourc:[1,2,3,4,5,6],span:6,special:4,spider:1,stack:6,star:6,start:6,state:6,statement:6,still:6,storag:6,store:6,store_fast:6,store_glob:6,store_nam:6,storeinstruct:1,strconstant:1,stringti:4,subinstruct:1,subiter:6,submodul:[],subsequ:6,support:1,swap:6,switchinstruct:1,symbol:6,taken:6,target:6,target_arch:1,termin:6,terminateinstruct:1,test_bytecode_vm:2,than:6,them:6,thi:[1,6],third:6,three:6,togeth:6,too:6,top:6,tos1:6,tos2:6,total:6,traceback:6,tri:6,tupl:6,tupleti:4,two:6,ty1:4,ty2:4,type:[],type_constraint:4,type_inf:[],typeinf:4,typesolv:4,ugt:1,ult:1,underdeteremin:4,unifi:4,union:4,unpack:6,unpack_sequ:6,util:[],val:4,valid:[],valu:[],valueerror:1,var_num:6,variabl:6,varti:4,verifi:1,verify_arg:1,visit:[3,4,5],visit_addinstruct:[1,3],visit_allocainstruct:[1,3],visit_andinstruct:[1,3],visit_arg:4,visit_arithmeticshiftrightinstruct:[1,3],visit_assign:4,visit_attribut:4,visit_augassign:4,visit_basicblock:[1,3],visit_binop:[1,4],visit_bool:4,visit_branchinstruct:3,visit_cal:4,visit_callinstruct:[1,3],visit_castinstruct:[1,3],visit_compar:4,visit_conditionalbranchinstruct:[1,3],visit_divinstruct:[1,3],visit_extractelementinstruct:[1,3],visit_faddinstruct:[1,3],visit_fcmpinstruct:[1,3],visit_fdivinstruct:[1,3],visit_fmulinstruct:[1,3],visit_for:4,visit_fsubinstruct:[1,3],visit_func:4,visit_funct:[1,3],visit_functiondef:4,visit_gepinstruct:[1,3],visit_icmpinstruct:[1,3],visit_if:4,visit_index:4,visit_indirectbranchinstruct:[1,3],visit_insertelementinstruct:[1,3],visit_lambda:4,visit_list:4,visit_litbool:4,visit_litfloat:4,visit_litint:4,visit_litstr:4,visit_loadinstruct:[1,3],visit_logicalshiftrightinstruct:[1,3],visit_loop:4,visit_modul:[1,3,4],visit_mulinstruct:[1,3],visit_nam:4,visit_noop:4,visit_num:4,visit_orinstruct:[1,3],visit_pass:4,visit_phiinstruct:[1,3],visit_prim:4,visit_return:4,visit_returninstruct:[1,3],visit_selectinstruct:[1,3],visit_shiftleftinstruct:[1,3],visit_storeinstruct:[1,3],visit_str:4,visit_subinstruct:[1,3],visit_subscript:4,visit_switchinstruct:[1,3],visit_terminateinstruct:[1,3],visit_var:4,visit_xorinstruct:[1,3],visitor:[],when:6,where:6,whether:6,which:6,why:6,why_:6,why_silenc:6,with_cleanup:6,work:6,xorinstruct:1,yield:6,zap:6},titles:["Welcome to src&#8217;s documentation!","ir package","main module","optimizer package","pyjit package","utils package","vm package"],titleterms:{"function":1,base_ir_visitor:1,base_visitor:5,basicpass:3,codegen:[1,4],constant:1,content:[1,3,4,5,6],context:1,decor:4,document:0,except:1,indic:0,instruct:1,interpret:1,irbuild:1,main:2,modul:[1,2,3,4,5,6],node:4,optim:3,packag:[1,3,4,5,6],pass_support:3,passmanag:3,pretty_print:4,pyjit:4,src:0,submodul:[1,3,4,5,6],tabl:0,type:1,type_inf:4,util:[1,5],valid:1,valu:1,visitor:4,welcom:0}})