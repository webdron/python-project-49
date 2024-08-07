#!/usr/bin/env python3
import prompt


def game(goal, data):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    i = 0
    for check, question in data:
        print(goal)
        print(question)
        answer = type(check)((prompt.string('Your answer: ')))
        if check == answer:
            i += 1
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{check}'. Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')
