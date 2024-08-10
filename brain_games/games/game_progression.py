from random import randint


def gameprogression():
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
    quest = f"{spisok}"
    return (quest, cool)
