from random import randint


def calcgame():
    summinumn = ("+", "-", "*")
    count = randint(1, 10)
    count_2 = randint(1, 10)
    interpritator = summinumn[randint(0, len(summinumn) - 1)]
    quest = f'{count} {interpritator} {count_2}'
    coll = eval(f" {count} {interpritator} {count_2}")
    return (quest, coll)
