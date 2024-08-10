from brain_games.engine import rungame
from brain_games.games.game_even import evengame


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    rungame(QUESTION, evengame)
