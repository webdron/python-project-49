import random


def result_generate():
    quest_list = []
    n = random.randint(1, 5)
    n_start = random.randint(1, 10)
    next_elem = n_start + n
    quest_list.append(n_start)
    i = 0
    while i < 9:
        quest_list.append(next_elem)
        next_elem = next_elem + n
        i += 1
    rand_elem = random.choice(quest_list)
    index = quest_list.index(rand_elem)
    quest_list.pop(index)
    quest_list.insert(index, "..")
    result = rand_elem
    string_list = []
    for elem in quest_list:
        string_list.append(str(elem))
    final_list = ' '.join(string_list)
    print(f'Question: {final_list}')
    return result


goal = 'What number is missing in the progression?'
