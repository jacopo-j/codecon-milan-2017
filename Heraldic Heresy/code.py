#Problem        : Heraldic Heresy
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

METALS = ["O", "A"]
COLORS = ["a", "g", "s", "v", "p"]

matrix = []
for idx, row in enumerate(data[1:]):
    matrix.append([])
    for char in list(row):
        matrix[idx].append(char)

for _ in range(2):
    for row in matrix:
        for i in range(0, len(row) - 1):
            if (((row[i] in METALS)
                  and (row[i+1] in METALS)
                  and (row[i] != row[i+1]))
                 or ((row[i] in COLORS)
                  and (row[i+1] in COLORS)
                  and (row[i] != row[i+1]))):
                print("INVALID")
                sys.exit()
    matrix = zip(*matrix)

print("VALID")
