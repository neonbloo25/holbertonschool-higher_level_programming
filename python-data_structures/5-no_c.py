#!/usr/bin/python3

def no_c(my_string):
    Cs_and_desist = ['C', 'c']
    my_string = ''.join([char for char in my_string if char not in Cs_and_desist])
    return (my_string)
