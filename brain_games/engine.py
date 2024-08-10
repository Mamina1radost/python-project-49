import prompt
from brain_games.cli import welcome_user


def rungame(question, game):
    name = welcome_user()
    print(question)
    i = 0
    while i < 3:
        count, coll = game()
        print(f'Question: {count}')
        answer = prompt.string("Your answer: ")
        if answer == coll:
            print('Correct')
            i += 1
        else:
            print(f"""{answer} is wrong answer ;(. Correct answer was {coll}.
            Let's try again, {name}!""")
            break
    else:
        print(f"Congratulations, {name}!")
