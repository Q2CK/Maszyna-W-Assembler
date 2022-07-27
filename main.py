import time
import os
import parse

# File path
here = os.path.dirname(os.path.abspath(__file__))

# Input file
error = 1
while error == 1:
    try:
        # asm = open(os.path.join(here, input("Assembly file name: ")), "r")
        asm_filename = input("Assembly file name: ")
        asm = open(os.path.join(here, asm_filename), "r")
    except:
        print("File not found\n")
    else:
        error = 0

# Output file
out_bin = open(os.path.join(here, f"bin_{asm_filename}"), "w")
out_bin.write("LINE|INSTRUCTIONS\n\n")
out_hex = open(os.path.join(here, f"hex_{asm_filename}"), "w")
out_hex.write("LINE|INSTRUCTIONS\n\n")

line_nr = 0

while error == 0:
    error = parse.parse_line(asm.readline(), out_bin, out_hex, line_nr)
    line_nr += 1

# Finish
print("Succesfully saved to " + out_bin.name + ", " + out_hex.name)
asm.close()
out_bin.close()
out_hex.close()

time.sleep(2)