#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user

NUMBER_OF_ROUNDS = 3


def engine(game):
    name = welcome_user()
    i = 0
    while i < NUMBER_OF_ROUNDS:
        print(game.GOAL)
        data = game.get_question_and_right_answer()
        result = data[0]
        question = data[1]
        print(question)
        answer = type(result)((prompt.string('Your answer: ')))
        if result == answer:
            i += 1
            print("Correct!")
        else:
            return print(f"'{answer}' is wrong answer ;(. "
                         f"Correct answer was '{result}'. Let's try again, {name}!")
    print(f'Congratulations, {name}!')
