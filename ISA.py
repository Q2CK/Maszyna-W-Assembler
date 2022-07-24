class ISA:
    def __init__(self, opcode_number, arg_lengths):
        self.arg_lengths = arg_lengths
        self.opcode_length = len(opcode_number)
        self.opcode_number = opcode_number

