# Copyright 2018 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  34: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  42: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  69: "THIN_STRING_TYPE",
  72: "ONE_BYTE_STRING_TYPE",
  73: "CONS_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  75: "SLICED_ONE_BYTE_STRING_TYPE",
  77: "THIN_ONE_BYTE_STRING_TYPE",
  82: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  98: "UNCACHED_EXTERNAL_STRING_TYPE",
  106: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  114: "UNCACHED_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_BIGINT64_ARRAY_TYPE",
  149: "FIXED_BIGUINT64_ARRAY_TYPE",
  150: "FIXED_DOUBLE_ARRAY_TYPE",
  151: "FEEDBACK_METADATA_TYPE",
  152: "FILLER_TYPE",
  153: "ACCESS_CHECK_INFO_TYPE",
  154: "ACCESSOR_INFO_TYPE",
  155: "ACCESSOR_PAIR_TYPE",
  156: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  157: "ALLOCATION_MEMENTO_TYPE",
  158: "ASYNC_GENERATOR_REQUEST_TYPE",
  159: "DEBUG_INFO_TYPE",
  160: "FUNCTION_TEMPLATE_INFO_TYPE",
  161: "INTERCEPTOR_INFO_TYPE",
  162: "INTERPRETER_DATA_TYPE",
  163: "MODULE_INFO_ENTRY_TYPE",
  164: "MODULE_TYPE",
  165: "OBJECT_TEMPLATE_INFO_TYPE",
  166: "PROMISE_CAPABILITY_TYPE",
  167: "PROMISE_REACTION_TYPE",
  168: "PROTOTYPE_INFO_TYPE",
  169: "SCRIPT_TYPE",
  170: "STACK_FRAME_INFO_TYPE",
  171: "TUPLE2_TYPE",
  172: "TUPLE3_TYPE",
  173: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  174: "WASM_DEBUG_INFO_TYPE",
  175: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  176: "CALLABLE_TASK_TYPE",
  177: "CALLBACK_TASK_TYPE",
  178: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  179: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  180: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  181: "MICROTASK_QUEUE_TYPE",
  182: "ALLOCATION_SITE_TYPE",
  183: "FIXED_ARRAY_TYPE",
  184: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  185: "HASH_TABLE_TYPE",
  186: "ORDERED_HASH_MAP_TYPE",
  187: "ORDERED_HASH_SET_TYPE",
  188: "NAME_DICTIONARY_TYPE",
  189: "GLOBAL_DICTIONARY_TYPE",
  190: "NUMBER_DICTIONARY_TYPE",
  191: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  192: "STRING_TABLE_TYPE",
  193: "EPHEMERON_HASH_TABLE_TYPE",
  194: "SCOPE_INFO_TYPE",
  195: "SCRIPT_CONTEXT_TABLE_TYPE",
  196: "BLOCK_CONTEXT_TYPE",
  197: "CATCH_CONTEXT_TYPE",
  198: "DEBUG_EVALUATE_CONTEXT_TYPE",
  199: "EVAL_CONTEXT_TYPE",
  200: "FUNCTION_CONTEXT_TYPE",
  201: "MODULE_CONTEXT_TYPE",
  202: "NATIVE_CONTEXT_TYPE",
  203: "SCRIPT_CONTEXT_TYPE",
  204: "WITH_CONTEXT_TYPE",
  205: "WEAK_FIXED_ARRAY_TYPE",
  206: "DESCRIPTOR_ARRAY_TYPE",
  207: "TRANSITION_ARRAY_TYPE",
  208: "CALL_HANDLER_INFO_TYPE",
  209: "CELL_TYPE",
  210: "CODE_DATA_CONTAINER_TYPE",
  211: "FEEDBACK_CELL_TYPE",
  212: "FEEDBACK_VECTOR_TYPE",
  213: "LOAD_HANDLER_TYPE",
  214: "PRE_PARSED_SCOPE_DATA_TYPE",
  215: "PROPERTY_ARRAY_TYPE",
  216: "PROPERTY_CELL_TYPE",
  217: "SHARED_FUNCTION_INFO_TYPE",
  218: "SMALL_ORDERED_HASH_MAP_TYPE",
  219: "SMALL_ORDERED_HASH_SET_TYPE",
  220: "STORE_HANDLER_TYPE",
  221: "UNCOMPILED_DATA_WITHOUT_PRE_PARSED_SCOPE_TYPE",
  222: "UNCOMPILED_DATA_WITH_PRE_PARSED_SCOPE_TYPE",
  223: "WEAK_ARRAY_LIST_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1064: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1065: "JS_DATE_TYPE",
  1066: "JS_ERROR_TYPE",
  1067: "JS_GENERATOR_OBJECT_TYPE",
  1068: "JS_MAP_TYPE",
  1069: "JS_MAP_KEY_ITERATOR_TYPE",
  1070: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1071: "JS_MAP_VALUE_ITERATOR_TYPE",
  1072: "JS_MESSAGE_OBJECT_TYPE",
  1073: "JS_PROMISE_TYPE",
  1074: "JS_REGEXP_TYPE",
  1075: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1076: "JS_SET_TYPE",
  1077: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1078: "JS_SET_VALUE_ITERATOR_TYPE",
  1079: "JS_STRING_ITERATOR_TYPE",
  1080: "JS_WEAK_MAP_TYPE",
  1081: "JS_WEAK_SET_TYPE",
  1082: "JS_TYPED_ARRAY_TYPE",
  1083: "JS_DATA_VIEW_TYPE",
  1084: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1085: "JS_INTL_COLLATOR_TYPE",
  1086: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1087: "JS_INTL_LIST_FORMAT_TYPE",
  1088: "JS_INTL_LOCALE_TYPE",
  1089: "JS_INTL_NUMBER_FORMAT_TYPE",
  1090: "JS_INTL_PLURAL_RULES_TYPE",
  1091: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1092: "WASM_EXCEPTION_TYPE",
  1093: "WASM_GLOBAL_TYPE",
  1094: "WASM_INSTANCE_TYPE",
  1095: "WASM_MEMORY_TYPE",
  1096: "WASM_MODULE_TYPE",
  1097: "WASM_TABLE_TYPE",
  1098: "JS_BOUND_FUNCTION_TYPE",
  1099: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("RO_SPACE", 0x02201): (138, "FreeSpaceMap"),
  ("RO_SPACE", 0x02251): (132, "MetaMap"),
  ("RO_SPACE", 0x022d1): (131, "NullMap"),
  ("RO_SPACE", 0x02341): (206, "DescriptorArrayMap"),
  ("RO_SPACE", 0x023a1): (205, "WeakFixedArrayMap"),
  ("RO_SPACE", 0x023f1): (152, "OnePointerFillerMap"),
  ("RO_SPACE", 0x02441): (152, "TwoPointerFillerMap"),
  ("RO_SPACE", 0x024c1): (131, "UninitializedMap"),
  ("RO_SPACE", 0x02531): (8, "OneByteInternalizedStringMap"),
  ("RO_SPACE", 0x025d1): (131, "UndefinedMap"),
  ("RO_SPACE", 0x02631): (129, "HeapNumberMap"),
  ("RO_SPACE", 0x026b1): (131, "TheHoleMap"),
  ("RO_SPACE", 0x02759): (131, "BooleanMap"),
  ("RO_SPACE", 0x02831): (136, "ByteArrayMap"),
  ("RO_SPACE", 0x02881): (183, "FixedArrayMap"),
  ("RO_SPACE", 0x028d1): (183, "FixedCOWArrayMap"),
  ("RO_SPACE", 0x02921): (185, "HashTableMap"),
  ("RO_SPACE", 0x02971): (128, "SymbolMap"),
  ("RO_SPACE", 0x029c1): (72, "OneByteStringMap"),
  ("RO_SPACE", 0x02a11): (194, "ScopeInfoMap"),
  ("RO_SPACE", 0x02a61): (217, "SharedFunctionInfoMap"),
  ("RO_SPACE", 0x02ab1): (133, "CodeMap"),
  ("RO_SPACE", 0x02b01): (200, "FunctionContextMap"),
  ("RO_SPACE", 0x02b51): (209, "CellMap"),
  ("RO_SPACE", 0x02ba1): (216, "GlobalPropertyCellMap"),
  ("RO_SPACE", 0x02bf1): (135, "ForeignMap"),
  ("RO_SPACE", 0x02c41): (207, "TransitionArrayMap"),
  ("RO_SPACE", 0x02c91): (212, "FeedbackVectorMap"),
  ("RO_SPACE", 0x02d31): (131, "ArgumentsMarkerMap"),
  ("RO_SPACE", 0x02dd1): (131, "ExceptionMap"),
  ("RO_SPACE", 0x02e71): (131, "TerminationExceptionMap"),
  ("RO_SPACE", 0x02f19): (131, "OptimizedOutMap"),
  ("RO_SPACE", 0x02fb9): (131, "StaleRegisterMap"),
  ("RO_SPACE", 0x03029): (202, "NativeContextMap"),
  ("RO_SPACE", 0x03079): (201, "ModuleContextMap"),
  ("RO_SPACE", 0x030c9): (199, "EvalContextMap"),
  ("RO_SPACE", 0x03119): (203, "ScriptContextMap"),
  ("RO_SPACE", 0x03169): (196, "BlockContextMap"),
  ("RO_SPACE", 0x031b9): (197, "CatchContextMap"),
  ("RO_SPACE", 0x03209): (204, "WithContextMap"),
  ("RO_SPACE", 0x03259): (198, "DebugEvaluateContextMap"),
  ("RO_SPACE", 0x032a9): (195, "ScriptContextTableMap"),
  ("RO_SPACE", 0x032f9): (151, "FeedbackMetadataArrayMap"),
  ("RO_SPACE", 0x03349): (183, "ArrayListMap"),
  ("RO_SPACE", 0x03399): (130, "BigIntMap"),
  ("RO_SPACE", 0x033e9): (184, "ObjectBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x03439): (137, "BytecodeArrayMap"),
  ("RO_SPACE", 0x03489): (210, "CodeDataContainerMap"),
  ("RO_SPACE", 0x034d9): (150, "FixedDoubleArrayMap"),
  ("RO_SPACE", 0x03529): (189, "GlobalDictionaryMap"),
  ("RO_SPACE", 0x03579): (211, "ManyClosuresCellMap"),
  ("RO_SPACE", 0x035c9): (183, "ModuleInfoMap"),
  ("RO_SPACE", 0x03619): (134, "MutableHeapNumberMap"),
  ("RO_SPACE", 0x03669): (188, "NameDictionaryMap"),
  ("RO_SPACE", 0x036b9): (211, "NoClosuresCellMap"),
  ("RO_SPACE", 0x03709): (190, "NumberDictionaryMap"),
  ("RO_SPACE", 0x03759): (211, "OneClosureCellMap"),
  ("RO_SPACE", 0x037a9): (186, "OrderedHashMapMap"),
  ("RO_SPACE", 0x037f9): (187, "OrderedHashSetMap"),
  ("RO_SPACE", 0x03849): (214, "PreParsedScopeDataMap"),
  ("RO_SPACE", 0x03899): (215, "PropertyArrayMap"),
  ("RO_SPACE", 0x038e9): (208, "SideEffectCallHandlerInfoMap"),
  ("RO_SPACE", 0x03939): (208, "SideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x03989): (208, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x039d9): (191, "SimpleNumberDictionaryMap"),
  ("RO_SPACE", 0x03a29): (183, "SloppyArgumentsElementsMap"),
  ("RO_SPACE", 0x03a79): (218, "SmallOrderedHashMapMap"),
  ("RO_SPACE", 0x03ac9): (219, "SmallOrderedHashSetMap"),
  ("RO_SPACE", 0x03b19): (192, "StringTableMap"),
  ("RO_SPACE", 0x03b69): (221, "UncompiledDataWithoutPreParsedScopeMap"),
  ("RO_SPACE", 0x03bb9): (222, "UncompiledDataWithPreParsedScopeMap"),
  ("RO_SPACE", 0x03c09): (223, "WeakArrayListMap"),
  ("RO_SPACE", 0x03c59): (193, "EphemeronHashTableMap"),
  ("RO_SPACE", 0x03ca9): (106, "NativeSourceStringMap"),
  ("RO_SPACE", 0x03cf9): (64, "StringMap"),
  ("RO_SPACE", 0x03d49): (73, "ConsOneByteStringMap"),
  ("RO_SPACE", 0x03d99): (65, "ConsStringMap"),
  ("RO_SPACE", 0x03de9): (77, "ThinOneByteStringMap"),
  ("RO_SPACE", 0x03e39): (69, "ThinStringMap"),
  ("RO_SPACE", 0x03e89): (67, "SlicedStringMap"),
  ("RO_SPACE", 0x03ed9): (75, "SlicedOneByteStringMap"),
  ("RO_SPACE", 0x03f29): (66, "ExternalStringMap"),
  ("RO_SPACE", 0x03f79): (82, "ExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x03fc9): (74, "ExternalOneByteStringMap"),
  ("RO_SPACE", 0x04019): (98, "UncachedExternalStringMap"),
  ("RO_SPACE", 0x04069): (114, "UncachedExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x040b9): (0, "InternalizedStringMap"),
  ("RO_SPACE", 0x04109): (2, "ExternalInternalizedStringMap"),
  ("RO_SPACE", 0x04159): (18, "ExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x041a9): (10, "ExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x041f9): (34, "UncachedExternalInternalizedStringMap"),
  ("RO_SPACE", 0x04249): (50, "UncachedExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x04299): (42, "UncachedExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x042e9): (106, "UncachedExternalOneByteStringMap"),
  ("RO_SPACE", 0x04339): (140, "FixedUint8ArrayMap"),
  ("RO_SPACE", 0x04389): (139, "FixedInt8ArrayMap"),
  ("RO_SPACE", 0x043d9): (142, "FixedUint16ArrayMap"),
  ("RO_SPACE", 0x04429): (141, "FixedInt16ArrayMap"),
  ("RO_SPACE", 0x04479): (144, "FixedUint32ArrayMap"),
  ("RO_SPACE", 0x044c9): (143, "FixedInt32ArrayMap"),
  ("RO_SPACE", 0x04519): (145, "FixedFloat32ArrayMap"),
  ("RO_SPACE", 0x04569): (146, "FixedFloat64ArrayMap"),
  ("RO_SPACE", 0x045b9): (147, "FixedUint8ClampedArrayMap"),
  ("RO_SPACE", 0x04609): (149, "FixedBigUint64ArrayMap"),
  ("RO_SPACE", 0x04659): (148, "FixedBigInt64ArrayMap"),
  ("RO_SPACE", 0x046a9): (131, "SelfReferenceMarkerMap"),
  ("RO_SPACE", 0x04711): (171, "Tuple2Map"),
  ("RO_SPACE", 0x047b1): (173, "ArrayBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x04aa1): (161, "InterceptorInfoMap"),
  ("RO_SPACE", 0x04b91): (169, "ScriptMap"),
  ("RO_SPACE", 0x04c59): (181, "MicrotaskQueueMap"),
  ("RO_SPACE", 0x08d41): (154, "AccessorInfoMap"),
  ("RO_SPACE", 0x08d91): (153, "AccessCheckInfoMap"),
  ("RO_SPACE", 0x08de1): (155, "AccessorPairMap"),
  ("RO_SPACE", 0x08e31): (156, "AliasedArgumentsEntryMap"),
  ("RO_SPACE", 0x08e81): (157, "AllocationMementoMap"),
  ("RO_SPACE", 0x08ed1): (158, "AsyncGeneratorRequestMap"),
  ("RO_SPACE", 0x08f21): (159, "DebugInfoMap"),
  ("RO_SPACE", 0x08f71): (160, "FunctionTemplateInfoMap"),
  ("RO_SPACE", 0x08fc1): (162, "InterpreterDataMap"),
  ("RO_SPACE", 0x09011): (163, "ModuleInfoEntryMap"),
  ("RO_SPACE", 0x09061): (164, "ModuleMap"),
  ("RO_SPACE", 0x090b1): (165, "ObjectTemplateInfoMap"),
  ("RO_SPACE", 0x09101): (166, "PromiseCapabilityMap"),
  ("RO_SPACE", 0x09151): (167, "PromiseReactionMap"),
  ("RO_SPACE", 0x091a1): (168, "PrototypeInfoMap"),
  ("RO_SPACE", 0x091f1): (170, "StackFrameInfoMap"),
  ("RO_SPACE", 0x09241): (172, "Tuple3Map"),
  ("RO_SPACE", 0x09291): (174, "WasmDebugInfoMap"),
  ("RO_SPACE", 0x092e1): (175, "WasmExportedFunctionDataMap"),
  ("RO_SPACE", 0x09331): (176, "CallableTaskMap"),
  ("RO_SPACE", 0x09381): (177, "CallbackTaskMap"),
  ("RO_SPACE", 0x093d1): (178, "PromiseFulfillReactionJobTaskMap"),
  ("RO_SPACE", 0x09421): (179, "PromiseRejectReactionJobTaskMap"),
  ("RO_SPACE", 0x09471): (180, "PromiseResolveThenableJobTaskMap"),
  ("RO_SPACE", 0x094c1): (182, "AllocationSiteMap"),
  ("RO_SPACE", 0x09511): (182, "AllocationSiteMap"),
  ("MAP_SPACE", 0x02201): (1057, "ExternalMap"),
  ("MAP_SPACE", 0x02251): (1072, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("RO_SPACE", 0x022a1): "NullValue",
  ("RO_SPACE", 0x02321): "EmptyDescriptorArray",
  ("RO_SPACE", 0x02491): "UninitializedValue",
  ("RO_SPACE", 0x025a1): "UndefinedValue",
  ("RO_SPACE", 0x02621): "NanValue",
  ("RO_SPACE", 0x02681): "TheHoleValue",
  ("RO_SPACE", 0x02719): "HoleNanValue",
  ("RO_SPACE", 0x02729): "TrueValue",
  ("RO_SPACE", 0x027d9): "FalseValue",
  ("RO_SPACE", 0x02821): "empty_string",
  ("RO_SPACE", 0x02ce1): "EmptyScopeInfo",
  ("RO_SPACE", 0x02cf1): "EmptyFixedArray",
  ("RO_SPACE", 0x02d01): "ArgumentsMarker",
  ("RO_SPACE", 0x02da1): "Exception",
  ("RO_SPACE", 0x02e41): "TerminationException",
  ("RO_SPACE", 0x02ee9): "OptimizedOut",
  ("RO_SPACE", 0x02f89): "StaleRegister",
  ("RO_SPACE", 0x04771): "EmptyByteArray",
  ("RO_SPACE", 0x04801): "EmptyFixedUint8Array",
  ("RO_SPACE", 0x04821): "EmptyFixedInt8Array",
  ("RO_SPACE", 0x04841): "EmptyFixedUint16Array",
  ("RO_SPACE", 0x04861): "EmptyFixedInt16Array",
  ("RO_SPACE", 0x04881): "EmptyFixedUint32Array",
  ("RO_SPACE", 0x048a1): "EmptyFixedInt32Array",
  ("RO_SPACE", 0x048c1): "EmptyFixedFloat32Array",
  ("RO_SPACE", 0x048e1): "EmptyFixedFloat64Array",
  ("RO_SPACE", 0x04901): "EmptyFixedUint8ClampedArray",
  ("RO_SPACE", 0x04961): "EmptySloppyArgumentsElements",
  ("RO_SPACE", 0x04981): "EmptySlowElementDictionary",
  ("RO_SPACE", 0x049c9): "EmptyOrderedHashMap",
  ("RO_SPACE", 0x049f1): "EmptyOrderedHashSet",
  ("RO_SPACE", 0x04a29): "EmptyPropertyCell",
  ("RO_SPACE", 0x04b09): "InfinityValue",
  ("RO_SPACE", 0x04b19): "MinusZeroValue",
  ("RO_SPACE", 0x04b29): "MinusInfinityValue",
  ("RO_SPACE", 0x04b39): "SelfReferenceMarker",
  ("OLD_SPACE", 0x02211): "EmptyScript",
  ("OLD_SPACE", 0x02291): "ManyClosuresCell",
  ("OLD_SPACE", 0x022b1): "NoElementsProtector",
  ("OLD_SPACE", 0x022d9): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x022e9): "ArraySpeciesProtector",
  ("OLD_SPACE", 0x02311): "TypedArraySpeciesProtector",
  ("OLD_SPACE", 0x02339): "PromiseSpeciesProtector",
  ("OLD_SPACE", 0x02361): "StringLengthProtector",
  ("OLD_SPACE", 0x02371): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x02399): "ArrayBufferNeuteringProtector",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
