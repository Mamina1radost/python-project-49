from brain_games.engine import rungame
from brain_games.games.game_progression import gameprogression


QUESTION = "What number is missing in the progression?"


def progression():
    rungame(QUESTION, gameprogression)
