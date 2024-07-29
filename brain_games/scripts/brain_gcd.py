import prompt
import math
from random import randint
from brain_games.cli import welcome_user


def gcd():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    i = 0
    while i < 3:
        count = randint(1, 100)
        count_2 = randint(1, 100)
        print(f"Question: {count} {count_2}")
        cool = math.gcd(count, count_2)
        answer = prompt.string("Your answer: ")
        if int(answer) == cool:
            print("Correct!")
            i += 1
        elif int(answer) != cool:
            print(f"{answer} is wrong answer ;(. Correct answer was {cool}.\nLet'stry again {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
