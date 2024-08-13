#!/usr/bin/env python3
import random
import operator


def check_generate():
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    oper_list = ['+', '-', '*']
    rand_oper = random.choice(oper_list)
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    check = (ops[rand_oper](n1, n2))
    print(f"Question: {n1} {rand_oper} {n2}")
    return check


goal = 'What is the result of the expression?'
