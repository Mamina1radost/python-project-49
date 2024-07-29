import prompt
from random import randint
from brain_games.cli import welcome_user


def even():
    name = welcome_user()
    i = 0
    print('Answer "yes" if the number is even, otherwise answer "no"')
    while i < 3:
        count = randint(1, 100)
        print(f"Question: {count}")
        if count % 2 == 0:
            coll = "yes"
        elif count % 2 == 1:
            coll = "no"
        answer = prompt.string("Your answer: ")
        if answer == coll:
            print("Correct")
            i += 1
        else:
            print(
                f"{answer} is wrong answer ;(. Correct answer was {coll}.\nLet's try again, {name}!"
            )
            break
    else:
        print(f"Congratulations, {name}!")
