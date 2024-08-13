import random


def result_generate():
    n = random.randint(1, 100)
    divider = 2
    remainder = 1
    while remainder != 0:
        remainder = n % divider
        divider = divider + 1
    if n > 1 or (divider == n + 1 and remainder == 0):
        result = 'yes'
    else:
        result = 'no'
    print(f"Question: {n}")
    return result


goal = 'Answer "yes" if given number is prime. Otherwise answer "no".'
