#!/usr/bin/env python3
import random
from brain_games.engine import game


def brain_prime():
    goal = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    check_list = []
    questions = []
    i = 0
    while i < 3:
        n = random.randint(1, 100)
        div = 2
        res = 1
        if n <= 1:
            check_list.append('no')
        else:
            while res != 0:
                res = n % div
                div = div + 1
            if div == n + 1 and res == 0:
                check_list.append('yes')
            else:
                check_list.append('no')
        questions.append(f"Question: {n}")
        i += 1

    data = zip(check_list, questions)
    game(goal, data)
