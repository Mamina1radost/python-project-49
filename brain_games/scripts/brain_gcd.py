from brain_games.engine import rungame
from brain_games.games.game_gcd import gsdgame


QUESTION = "Find the greatest common divisor of given numbers."


def gcd():
    rungame(QUESTION, gsdgame)
