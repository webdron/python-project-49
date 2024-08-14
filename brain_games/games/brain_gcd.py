import random
import math

GOAL = 'Find the greatest common divisor of given numbers.'


def get_question_and_right_answer():
    data = []
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    data.append(math.gcd(n1, n2))
    data.append(f"Question: {n1} {n2}")
    return data
