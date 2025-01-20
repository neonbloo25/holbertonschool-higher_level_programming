#!/usr/bin/python3
for i in range(0, 100):
    # chooses when to stop with commas
    if i != 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
