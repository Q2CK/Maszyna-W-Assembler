import ISA

# ISA.ISA(<opcode output string>, [<argument lengths list (negative if fill with 0s)>])
instruction_length = 12

op_codes = {
    "STP": ISA.ISA("00000000", [-4]),
    "SLP": ISA.ISA("00000001", [-4]),
    "GUW": ISA.ISA("00000010", [-4]),
    "CFT": ISA.ISA("00000011", [-4]),
    "CFF": ISA.ISA("00000100", [-4]),
    "RTN": ISA.ISA("00000101", [-4]),
    "RSH": ISA.ISA("00000110", [-4]),
    "NIN": ISA.ISA("00000111", [-2, 2]),
    "AIN": ISA.ISA("00001000", [-2, 2]),
    "CIN": ISA.ISA("00001001", [-2, 2]),
    "RIN": ISA.ISA("00001010", [-2, 2]),
    "GIN": ISA.ISA("00001011", [-2, 2]),
    "ADD": ISA.ISA("0001", [8]),
    "SUB": ISA.ISA("0010", [8]),
    "AND": ISA.ISA("0011", [8]),
    "IOR": ISA.ISA("0100", [8]),
    "XOR": ISA.ISA("0101", [8]),
    "CAL": ISA.ISA("0110", [8]),
    "PUS": ISA.ISA("0111", [8]),
    "POP": ISA.ISA("1000", [8]),
    "LOD": ISA.ISA("1001", [8]),
    "STR": ISA.ISA("1010", [8]),
    "JMF": ISA.ISA("1011", [8]),
    "JMP": ISA.ISA("1100", [8]),
    "JMO": ISA.ISA("1101", [8]),
    "JMM": ISA.ISA("1110", [8]),
    "JMZ": ISA.ISA("1111", [8]),
}
