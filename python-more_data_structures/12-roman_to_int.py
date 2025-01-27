#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0
    s1 = "Invalid character '"
    s2 = "' in Roman numeral string."

    for i in range(len(roman_string)):
        if roman_string[i] not in roman_dict:
            raise ValueError("{}{}{}".format(s1, roman_string[i], s2))

        current_value = roman_dict[roman_string[i]]
        try:
            next_value = roman_dict[roman_string[i + 1]]
        except IndexError:
            next_value = 0

        if current_value < next_value:
            num -= current_value
        else:
            num += current_value

    return num
