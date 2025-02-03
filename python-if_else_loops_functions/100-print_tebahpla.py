#!/usr/bin/python3
"""Print reverse alphabet using ASCIIs alternating(zYx...A)"""


def tebahpla():
    result = ""
    teba1 = 122  # ASCII for 'z'
    teba2 = 90   # ASCII for 'Z'

    while teba1 > 64:
        result += chr(teba1)
        teba1 -= 1
        if teba1 > 64:
            result += chr(teba2)
        teba2 -= 1

    print(result, end="")


tebahpla()
