import random

from brain_games.engine import game

goal = 'Answer "yes" if the number is even, otherwise answer "no".'
check_list = []
questions = []
i = 0
while i < 3:
    n = random.randint(1, 100)
    if n % 2 == 0:
        check_list.append('yes')
    else:
        check_list.append('no')
    questions.append(f"Question: {n}")
    i += 1
data = zip(check_list, questions)
game(goal, data)
