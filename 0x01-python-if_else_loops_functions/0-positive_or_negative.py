#!/usr/bin/python3
import random
number = random.choice([-98, 98])
if number > 0:
    print(f"{number:d} is positive")
elif number == 0:
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is negative")
