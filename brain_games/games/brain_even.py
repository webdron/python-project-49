#!/usr/bin/env python3
import random


def check_generate():
    n = random.randint(1, 100)
    if n % 2 == 0:
        check = 'yes'
    else:
        check = 'no'
    print(f"Question: {n}")
    return check


goal = 'Answer "yes" if the number is even, otherwise answer "no".'
