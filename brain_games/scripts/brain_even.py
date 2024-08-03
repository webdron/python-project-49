import random
import prompt


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    check = ''
    i = 0
    while i < 3:
        n = random.randint(1, 100)
        if n % 2 == 0:
            check = 'yes'
        else:
            check = 'no'
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print(f"Question: {n}")
        answer = prompt.string('Your answer: ')
        if check == answer:
            i += 1
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{check}'. Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')

brain_even()