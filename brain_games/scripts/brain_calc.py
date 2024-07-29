from random import randint
from brain_games.cli import welcome_user
import prompt


def calc():
    name = welcome_user()
    summinumn = ("+", "-", "*")
    print("What is the result of the expression?")
    i = 0

    while i < 3:
        count = randint(1, 10)
        count_2 = randint(1, 10)
        interpritator = summinumn[randint(0, len(summinumn) - 1)]
        print(f"Question: {count} {interpritator} {count_2}")
        cool = eval(f" {count} {interpritator} {count_2}")
        answer = prompt.string("Your answer: ")
        if cool == int(answer):
            print("Correct!")
            i += 1
        elif cool != int(answer):
            print(f"{answer} is wrong answer ;(. Correct answer was '{cool}'.\nLet's try again, {name}")
            break
    else:
        print(f"Congratulations, {name}!")
