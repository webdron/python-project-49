#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user

NUMBER_OF_ROUNDS = 3


def engine(game):
    name = welcome_user()
    i = 0
    while i < NUMBER_OF_ROUNDS:
        print(game.GOAL)
        right_answer, question = game.get_question_and_right_answer()
        print(question)
        answer = prompt.string('Your answer: ')
        if right_answer == answer:
            i += 1
            print("Correct!")
        else:
            return (
                print(f"'{answer}' is wrong answer ;(."
                         f"Correct answer was '{right_answer}'."
                         f"Let's try again, {name}!"))
    print(f'Congratulations, {name}!')
