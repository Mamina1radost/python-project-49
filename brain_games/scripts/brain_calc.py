from brain_games.engine import rungame
from brain_games.games.game_calc import calcgame


QUESTION = "What is the result of the expression?"


def calc():
    rungame(QUESTION, calcgame)
