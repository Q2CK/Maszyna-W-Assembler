import time
import os
import parse

# File path
here = os.path.dirname(os.path.abspath(__file__))

# Input file
error = 1
while(error == 1):
    try:
        # asm = open(os.path.join(here, input("Assembly file name: ")), "r")
        asm = open(os.path.join(here, "test.txt"), "r")
    except:
        print("File not found\n")
    else:
        error = 0

# Output file
# out_hex = open(os.path.join(here, input("Hexadecimal file name: ")), "w")
out_hex = open(os.path.join(here, "hex_test.txt"), "w")
out_hex.write("LINE|INSTRUCTIONS\n\n")

line_nr = 0
out_bin.write("LINE|INSTRUCTIONS\n\n")

while(error == 0):
    error = parse(asm.readline(), out_bin, line_nr)
    line_nr += 1

# Finish
print("Succesfully saved to " + out_hex.name)
asm.close()
out_hex.close()

time.sleep(2)