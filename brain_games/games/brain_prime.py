import random

GOAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    divider = 2
    remainder = 1
    while remainder != 0:
        remainder = n % divider
        divider = divider + 1
    return divider == n + 1 and remainder == 0


def get_question_and_right_answer():
    n = random.randint(1, 100)
    right_answer = 'yes' if is_prime(n) else 'no'
    question = f"Question: {n}"
    return right_answer, question
