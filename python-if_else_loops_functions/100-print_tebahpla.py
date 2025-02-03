#!/usr/bin/python3
"""Print reverse alphabet using ASCIIs alternating(zYx...A)"""


def tebahpla():
    teba1 = 122
    teba2 = 90

    while teba1 > 64:
        if teba1 % 2 == 0 and teba2 % 2 == 0:
            print("{}".format(chr(teba1)), end="")
            teba2 -= 1
            teba1 -= 1
            continue
        print("{}".format(chr(teba2)), end="")
        teba2 -= 1
        teba1 -= 1

tebahpla();
