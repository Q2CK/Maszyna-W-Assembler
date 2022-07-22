import time
import os
here = os.path.dirname(os.path.abspath(__file__))

opcodes = {
    "STP": 0,
    "SLP": 0,
    "GUW": 0,
    "CFT": 0,
    "CFF": 0,
    "RTN": 0,
    "RSH": 0,
    "NIN": 0,
    "AIN": 0,
    "CIN": 0,
    "RIN": 0,
    "GIN": 0,
    "ADD": 1,
    "SUB": 2,
    "AND": 3,
    "IOR": 4,
    "XOR": 5,
    "CAL": 6,
    "PUS": 7,
    "POP": 8,
    "LOD": 9,
    "STR": 10,
    "JMF": 11,
    "JMP": 12,
    "JMO": 13,
    "JMM": 14,
    "JMZ": 15,
}

keys = list(opcodes)

def bin_write(file, q1, q2, q3, nr):
    file.write(format(nr, '03d') + ": " + q1 + " " + q2 + " " + q3 + "\n")

def hex_write(file, q1, q2, q3, nr):
    file.write(format(nr, '03d') + ": " + hex(int(q1, 2))[2].upper() + hex(int(q2, 2))[2].upper() + hex(int(q3, 2))[2].upper() + "\n")


def parse(file_line, output_file, nr):
    file_line = file_line.replace("\n", "")
    token = file_line.split(" ")

    if((token[0] in keys) and (keys.index(token[0]) in range(0, 7))):
        seg1 = format(opcodes[token[0]], '04b')
        seg2 = format(keys.index(token[0]), '04b')
        seg3 = "0000"
        bin_write(out_bin, seg1, seg2, seg3, nr)
        hex_write(out_hex, seg1, seg2, seg3, nr)
        return 0
    elif((token[0] in keys) and (keys.index(token[0]) in range(7, 12)) and (int(token[1]) in range(0, 4))):
        seg1 = format(opcodes[token[0]], '04b')
        seg2 = format(keys.index(token[0]), '04b')
        seg3 = "00" + format(int(token[1]), '02b')
        bin_write(out_bin, seg1, seg2, seg3, nr)
        hex_write(out_hex, seg1, seg2, seg3, nr)
        return 0
    elif((token[0] in keys) and (keys.index(token[0]) in range(12, 27)) and format(int(token[1]) in range(0, 255))):
        seg1 = format(opcodes[token[0]], '04b')
        seg2 = format(int(int(token[1])/16), '04b')
        seg3 = format(int(token[1]) % 16, '04b')
        bin_write(out_bin, seg1, seg2, seg3, nr)
        hex_write(out_hex, seg1, seg2, seg3, nr)
        return 0
    else:
        output_file.write(format(nr, '03d') + ": File end or unknown opcode\n")
        return 1

error = 1

while(error == 1):
    try:
        asm = open(os.path.join(here, input("Assembly file name: ")), "r")
    except:
        print("File not found\n")
    else:
        error = 0

out_bin = open(os.path.join(here, input("Binary file name: ")), "w")
out_hex = open(os.path.join(here, input("Hexadecimal file name: ")), "w")

line_nr = 0
out_bin.write("LINE|INSTRUCTIONS\n\n")

while(error == 0):
    error = parse(asm.readline(), out_bin, line_nr)
    line_nr += 1

print("Succesfully saved to " + out_bin.name)
asm.close()
out_bin.close()
out_hex.close()

time.sleep(2)


