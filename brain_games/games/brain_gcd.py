#!/usr/bin/env python3
import random


def check_generate():
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    if max(n1, n2) % min(n1, n2) == 0:
        check = (min(n1, n2))
        print(f"Question: {n1} {n2}")
    else:
        a = max(n1, n2)
        b = min(n1, n2)
        m = a % b
        while m != 0:
            a = m
            m = b % m
            b = a
        check = a
    print(f"Question: {n1} {n2}")
    return check


goal = 'Find the greatest common divisor of given numbers.'
