import ISA

# ISA.ISA(<opcode length>, <opcode output string>, [<argument lengths list (negative if fill with 0s)>])

op_codes = {
    "STP": ISA.ISA(8, "00", [-4]),
    "SLP": ISA.ISA(8, "01", [-4]),
    "GUW": ISA.ISA(8, "02", [-4]),
    "CFT": ISA.ISA(8, "03", [-4]),
    "CFF": ISA.ISA(8, "04", [-4]),
    "RTN": ISA.ISA(8, "05", [-4]),
    "RSH": ISA.ISA(8, "06", [-4]),
    "NIN": ISA.ISA(8, "07", [-2, 2]),
    "AIN": ISA.ISA(8, "08", [-2, 2]),
    "CIN": ISA.ISA(8, "09", [-2, 2]),
    "RIN": ISA.ISA(8, "0A", [-2, 2]),
    "GIN": ISA.ISA(8, "0B", [-2, 2]),
    "ADD": ISA.ISA(4, "1", [8]),
    "SUB": ISA.ISA(4, "2", [8]),
    "AND": ISA.ISA(4, "3", [8]),
    "IOR": ISA.ISA(4, "4", [8]),
    "XOR": ISA.ISA(4, "5", [8]),
    "CAL": ISA.ISA(4, "6", [8]),
    "PUS": ISA.ISA(4, "7", [8]),
    "POP": ISA.ISA(4, "8", [8]),
    "LOD": ISA.ISA(4, "9", [8]),
    "STR": ISA.ISA(4, "A", [8]),
    "JMF": ISA.ISA(4, "B", [8]),
    "JMP": ISA.ISA(4, "C", [8]),
    "JMO": ISA.ISA(4, "D", [8]),
    "JMM": ISA.ISA(4, "E", [8]),
    "JMZ": ISA.ISA(4, "F", [8]),
}
