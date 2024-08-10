from random import randint
import math


def gsdgame():
    count = randint(1, 100)
    count_2 = randint(1, 100)
    quest = f"{count} {count_2}"
    cool = math.gcd(count, count_2)
    return (quest, cool)
