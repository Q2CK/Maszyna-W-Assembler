import opcodes
import math

def parse_line(input, output_file, nr):
    input = input.replace("\n", "")
    token = input.split(" ")

    if token[0] not in opcodes.op_codes:
        return 1

    output_file.write(format(nr, '03d') + ": " + opcodes.op_codes[token[0]].opcode_number + "\n")

    return 0

