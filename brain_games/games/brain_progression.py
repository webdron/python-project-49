import random

GOAL = 'What number is missing in the progression?'


def get_question_and_right_answer():
    quest_list = [random.randint(1, 10)]
    n = random.randint(1, 5)
    i = 0
    while i < 9:
        quest_list.append(quest_list[i] + n)
        i += 1
    rand_elem = random.choice(quest_list)
    quest_list[quest_list.index(rand_elem)] = ".."
    final_list = ''
    for elem in quest_list:
        final_list = final_list + f' {str(elem)}'
    right_answer = rand_elem
    question = f'Question: {final_list.strip()}'
    return str(right_answer), question
