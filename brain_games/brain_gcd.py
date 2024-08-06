#!/usr/bin/env python3
import random
from brain_games.engine import game


def brain_gcd():
    goal = 'Find the greatest common divisor of given numbers.'
    check_list = []
    questions = []
    i = 0
    while i < 3:
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        if max(n1, n2) % min(n1, n2) == 0:
            check_list.append(min(n1, n2))
            questions.append(f"Question: {n1} {n2}")
        else:
            a = max(n1, n2)
            b = min(n1, n2)
            m = a % b
            while m != 0:
                a = m
                m = b % m
                b = a
            check_list.append(a)
        questions.append(f"Question: {n1} {n2}")
        i += 1
    data = zip(check_list, questions)
    game(goal, data)
