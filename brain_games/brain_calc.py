import random
import operator
from brain_games.engine import game

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
}
i = 0
check_list = []
questions = []
while i < 3:
    oper_list = ['+', '-', '*']
    rand_oper = random.choice(oper_list)
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    check_list.append(ops[rand_oper](n1, n2))
    questions.append(f"Question: {n1} {rand_oper} {n2}")
    i += 1
data = zip(check_list, questions)
goal = 'What is the result of the expression?'

game(goal, data)