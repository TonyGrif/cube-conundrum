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
        identification (int): The id of a game.
    """

    def __init__(self, id_num: int) -> None:
        """Constructor for the game class.

        Parameters:
            id_num (int): The id of this game.
        """
        self.identification = id_num

    @property
    def identification(self) -> int:
        """
        Return the identification of this game.

        Returns:
            identification (int): The identification number.
        """
        return self._identification

    @identification.setter
    def identification(self, id_num: int) -> None:
        """
        Set the id number of this Game.

        Parameters:
            identification (int): The id of this game.
        """
        self._identification = id_num
