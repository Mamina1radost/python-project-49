import prompt
from random import randint
from brain_games.cli import welcome_user


def progression():
    name = welcome_user()
    print("What number is missing in the progression?")
    i = 0
    while i < 3:
        start = randint(1, 5)
        step = randint(1, 5)
        stop = start + step * 10
        spisok = range(start, stop + step, step)
        spisok = list(spisok)
        index = randint(0, len(spisok) - 1)
        cool = spisok[index]
        spisok[index] = ".."
        spisok = map(str, spisok)
        spisok = " ".join(spisok)
        print(f"Question: {spisok}")
        answer = prompt.string("Your answer: ")
        if cool == int(answer):
            print("Correct")
            i += 1
        elif cool != int(answer):
            print(
                f"{answer} is wrong answer ;(. Correct answer was '{cool}'.\nLet's try again, {name}"
            )
            break
    else:
        print(f"Congratulations, {name}!")
