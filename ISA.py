class ISA:
    def __init__(self, opcode_length, opcode_number, arg_lengths):
        self.arg_lengths = arg_lengths
        self.opcode_length = opcode_length
        self.opcode_number = opcode_number

