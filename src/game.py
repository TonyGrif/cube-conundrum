"""This module contains the Game dataclass.
"""

import logging
import re
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Turn:
    """
    Turn dataclass for storing results of each turn.

    Attributes:
        red (int): The number of red cubes pulled.
        green (int): The number of green cubes pulled.
        blue (int): The number of blue cubes pulled.
    """

    red: int
    green: int
    blue: int


class Game:
    """
    Game class for storing game data.

    Attributes:
        identification (int): The id of a game.
        turns (list): The turns of a game.
    """

    def __init__(self, line: str) -> None:
        """Constructor for the game class.

        Parameters:
            line (str): String containing all the game data.
        """
        data = self.parse_line(line)
        self.identification = data[0]
        self.turns = data[1]

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

    def parse_line(self, line: str) -> Tuple[int, List[Turn]]:
        """
        Parse a line for turns of a game.

        Parameters:
            line (str): The line to parse. Game ID is
            to be ended by a colon and Turns
            are to be deliniated by semi-colons.

        Returns:
            A tuple containing the id and a list of Turns.
        """
        game_num = int("".join(re.findall(r"\d", line.split(":")[0])))
        logging.debug("Game ID: %s", game_num)

        raw_turns = line[line.find(":") + 1 : -1].split(";")
        # logging.debug("Raw Turns: %s", raw_turns)
        turns = []
        for turn in raw_turns:
            turns.append(self._parse_turns(turn))

        return (game_num, turns)

    def _parse_turns(self, line: str) -> Turn:
        """
        Parse a shortened line for turn data.

        Parameters:
            line (str): The line to parse.

        Returns:
            A turn object with the data in line.
        """
        red = re.search(r"(\d+)(?= r)", line)
        red = 0 if red is None else red.group()

        green = re.search(r"(\d+)(?= g)", line)
        green = 0 if green is None else green.group()

        blue = re.search(r"(\d+)(?= b)", line)
        blue = 0 if blue is None else blue.group()

        logging.debug("Turn created with rgb(%s, %s, %s)", red, green, blue)
        return Turn(int(red), int(green), int(blue))
