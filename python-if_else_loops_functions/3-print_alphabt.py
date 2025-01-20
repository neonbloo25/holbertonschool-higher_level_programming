#!/usr/bin/python3
# Uses ascii values to print the alphabet
for i in range(97, 123):
    # Modded to skip q and e
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
