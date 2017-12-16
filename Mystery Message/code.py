#Problem        : Mystery Message
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()[0].split(" ")

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

enc = data[0][0]
decr = data[-1][0]

e_idx = alphabet.index(enc)
d_idx = alphabet.index(decr)

offset = e_idx - d_idx

if (offset < 0):
    offset = 26 + offset

print(offset)
