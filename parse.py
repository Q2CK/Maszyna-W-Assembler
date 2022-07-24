import opcodes


def append_bits(token, instruction, bit_counter):
    out = ""
    i = 0
    i_token = 1
    while i in range(0, len(instruction.arg_lengths)):
        bit_counter += abs(instruction.arg_lengths[i])
        if instruction.arg_lengths[i] <= 0:
            out += "".ljust(abs(instruction.arg_lengths[i]), "0")
        else:
            out += format(int(token[i_token]), f'0{instruction.arg_lengths[i]}b')
            i_token += 1
        i += 1
    return out


def parse_line(input, bin_file, hex_file, nr):
    input = input.replace("\n", "")
    token = input.split(" ")

    if token[0] not in opcodes.op_codes:
        return 1
    else:
        instruction = opcodes.op_codes[token[0]]

    bit_counter = 0
    bin_line = ""
    bin_line += append_bits(token, instruction, bit_counter)

    line_number = (format(nr, '03d') + ": ")

    bin_file.write(line_number + instruction.opcode_number + bin_line + "\n")
    hex_file.write(line_number + format(int(instruction.opcode_number + bin_line, 2), '03x').upper() + "\n")

    return 0

