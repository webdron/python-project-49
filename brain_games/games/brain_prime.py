#!/usr/bin/env python3
import random


def check_generate():
    n = random.randint(1, 100)
    divider = 2
    result = 1
    if n <= 1:
        check = 'no'
    else:
        while result != 0:
            res = n % divider
            divider = divider + 1
        if divider == n + 1 and result == 0:
            check = 'yes'
        else:
            check = 'no'
    print(f"Question: {n}")
    return check


goal = 'Answer "yes" if given number is prime. Otherwise answer "no".'
