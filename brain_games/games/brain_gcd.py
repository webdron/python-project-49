import random
import math

GOAL = 'Find the greatest common divisor of given numbers.'


def get_question_and_right_answer():
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    right_answer = math.gcd(n1, n2)
    question = f"Question: {n1} {n2}"
    return str(right_answer), question
