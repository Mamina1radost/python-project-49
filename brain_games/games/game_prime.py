from random import randint


def function(count):
    if count <= 1:
        return "no"
    elif count > 1:
        for chislo in range(2, int(count**0.5) + 1):
            if count % chislo == 0:
                return "no"
        return "yes"


def primegame():
    count = randint(1, 100)
    cool = function(count)
    return (count, cool)
