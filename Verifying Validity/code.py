#Problem        : Verifying Validity
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

for isbn in data[1:]:
    characters = list(isbn)
    ssum = 0
    for idx, char in enumerate(characters):
        if (((idx + 1) % 2) == 0):
            mult = 3
        else:
            mult = 1
        mchar = int(char) * mult
        ssum += mchar
    if (ssum % 10 == 0):
        print("VALID")
    else:
        print("NOT VALID")
