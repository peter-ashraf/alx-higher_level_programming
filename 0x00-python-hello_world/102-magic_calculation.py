#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    return 98 + a ** b

# Check if the function behaves the same as the provided bytecode
a = 2
b = 3
expected_result = 98 + a ** b
assert magic_calculation(a, b) == expected_result


# Print the disassembled bytecode of the function
dis.dis(magic_calculation)

