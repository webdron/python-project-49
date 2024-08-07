#!/usr/bin/env python3
import random
from brain_games.engine import game


def brain_progression():
    goal = 'What number is missing in the progression?'
    check_list = []
    questions = []
    i = 0
    while i < 3:
        quest_list = []
        n = random.randint(1, 5)
        n_start = random.randint(1, 10)
        next_elem = n_start + n
        quest_list.append(n_start)
        j = 0
        while j < 9:
            quest_list.append(next_elem)
            next_elem = next_elem + n
            j += 1
        rand_elem = random.choice(quest_list)
        index = quest_list.index(rand_elem)
        quest_list.pop(index)
        quest_list.insert(index, "..")
        check_list.append(rand_elem)
        string_list = []
        for elem in quest_list:
            string_list.append(str(elem))
        final_list = ' '.join(string_list)
        questions.append(f'Question: {final_list}')
        i += 1

    data = zip(check_list, questions)
    game(goal, data)
