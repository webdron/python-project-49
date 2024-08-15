import random

GOAL = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    return n % 2 == 0


def get_question_and_right_answer():
    n = random.randint(1, 100)
    right_answer = 'yes' if is_even(n) else 'no'
    question = f"Question: {n}"
    return right_answer, question
