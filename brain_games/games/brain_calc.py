import random
import operator

GOAL = 'What is the result of the expression?'


def get_question_and_right_answer():
    data = []
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    operators_list = ['+', '-', '*']
    rand_operator = random.choice(operators_list)
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    data.append(ops[rand_operator](n1, n2))
    data.append(f"Question: {n1} {rand_operator} {n2}")
    return data
