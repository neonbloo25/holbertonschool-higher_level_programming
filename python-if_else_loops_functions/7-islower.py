#!/usr/bin/python3
def islower(c):
    # the following cross-checks it with ASCII values
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
