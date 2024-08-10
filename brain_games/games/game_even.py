from random import randint


def evengame():
    count = randint(1, 100)
    if count % 2 == 0:
        coll = "yes"
    elif count % 2 == 1:
        coll = "no"
    return (count, coll)
