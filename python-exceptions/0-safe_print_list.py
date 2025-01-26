#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    for r in range(x):
        try:
            print("{}".format(mylist[r]), end="")
            i += 1
        except IndexError:
            break
    print("")
    return (i)
