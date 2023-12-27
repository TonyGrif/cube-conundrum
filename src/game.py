"""This module contains the Game dataclass.
"""

from dataclasses import dataclass


@dataclass
class Turn:
    """Turn dataclass for storing results of each turn.

    Attributes:
        red (int): The number of red cubes pulled.
        green (int): The number of green cubes pulled.
        blue (int): The number of blue cubes pulled.
    """

    red: int
    green: int
    blue: int


class Game:
    """Game class for storing game data.

    Attributes:

    """

    def __init__(self):
        """Constructor for the game class."""
        pass
