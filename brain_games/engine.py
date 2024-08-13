#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user


def engine(mod):
    name = welcome_user()
    i = 0
    while i < 3:
        print(mod.goal)
        result = mod.result_generate()
        answer = type(result)((prompt.string('Your answer: ')))
        if result == answer:
            i += 1
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'. Let's try again, {name}!")
            break
        if i == 3:
            print(f'Congratulations, {name}!')
