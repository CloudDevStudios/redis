#!/usr/bin/env python3

# Outputs the generated part of src/fmtargs.h
MAX_ARGS = 120

import os
print("/* Everything below this line is automatically generated by")
print(" * %s. Do not manually edit. */\n" % os.path.basename(__file__))

print(
    '#define ARG_N('
    + ', '.join([f'_{str(i)}' for i in range(1, MAX_ARGS + 1, 1)])
    + ', N, ...) N'
)

print('\n#define RSEQ_N() ' + ', '.join([str(i) for i in range(MAX_ARGS, -1, -1)]))

print('\n#define COMPACT_FMT_2(fmt, value) fmt')
for i in range(4, MAX_ARGS + 1, 2):
    print(
        f'#define COMPACT_FMT_{i}(fmt, value, ...) fmt COMPACT_FMT_{i - 2}(__VA_ARGS__)'
    )

print('\n#define COMPACT_VALUES_2(fmt, value) value')
for i in range(4, MAX_ARGS + 1, 2):
    print(
        f'#define COMPACT_VALUES_{i}(fmt, value, ...) value, COMPACT_VALUES_{i - 2}(__VA_ARGS__)'
    )

print("\n#endif")
