from brain_games.engine import rungame
from brain_games.games.game_prime import primegame


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    rungame(QUESTION, primegame)
