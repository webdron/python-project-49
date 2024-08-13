#!/usr/bin/env python3
import random


def check_generate():
    n = random.randint(1, 100)
    div = 2
    res = 1
    if n <= 1:
        check = 'no'
    else:
        while res != 0:
            res = n % div
            div = div + 1
        if div == n + 1 and res == 0:
            check = 'yes'
        else:
            check = 'no'
    print(f"Question: {n}")
    return check


goal = 'Answer "yes" if given number is prime. Otherwise answer "no".'
