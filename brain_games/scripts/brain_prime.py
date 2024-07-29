import prompt
from brain_games.cli import welcome_user
from random import randint


def prime():
    name = welcome_user()
    i = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while i < 3:
        count = randint(1, 100)
        print(f"Question: {count}")

        if count <= 1:
            cool = "no"
        elif count > 1:
            for chislo in range(2, int(count**0.5) + 1):
                if count % chislo == 0:
                    cool = "no"
                    break
            else:
                cool = "yes"
        answer = prompt.string("Your answer: ")
        if answer == cool:
            print("Correct!")
            i += 1
        else:
            print(
                f"{answer} is wrong answer ;(. Correct answer was {cool}.\nLet's try again, {name}!"
            )
            break
    else:
        print(f"Congratulations, {name}!")
