import random


def result_generate():
    n = random.randint(1, 100)
    if n % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    print(f"Question: {n}")
    return result


goal = 'Answer "yes" if the number is even, otherwise answer "no".'
