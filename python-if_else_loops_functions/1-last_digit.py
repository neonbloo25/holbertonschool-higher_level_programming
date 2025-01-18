#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    lastD = number % 10
elif number < 0:
    lastD = number % -10

if lastD <= 5 and lastD != 0:
    print(f"Last digit of {number} is {lastD} and is less than 6 and not 0")
elif lastD == 0:
    print(f"Last digit of {number} is {lastD} and is 0")
else:
    print(f"Last digit of {number} is {lastD} and is greater than 5")
