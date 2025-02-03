#!/usr/bin/python3
"""Print reverse alphabet using ASCIIs alternating(zYx...A)"""


def tebahpla():
    teba1 = 122
    teba2 = 90
    tebahpla = ""

    while teba1 > 64:
        if teba1 % 2 == 0 and teba2 % 2 == 0:
            tebahpla += chr(teba1)
            teba2 -= 1
            teba1 -= 1
            continue
        tebahpla += chr(teba2)
        teba2 -= 1
        teba1 -= 1

        if len(tebahpla) == 26:
            break

    print(tebahpla, end="")


tebahpla()
