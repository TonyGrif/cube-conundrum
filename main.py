#!/usr/bin/env python3

"""This module contains the main driver of the Cube Conundrum project.
"""


import argparse
import logging
import sys
from pathlib import Path

from src.game import Game


def main():
    """Main driver of the Cube Conundrum project."""
    parser = argparse.ArgumentParser(
        prog="Cube Conundrum",
        description="Script to determine which sequences of games are valid.",
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Output all program debug logs to console.",
    )
    parser.add_argument("txt_file", type=Path, help="Text file to parse.")

    parser.add_argument(
        "--red",
        type=int,
        help="The number of acceptable red cubes for each game.",
        default=12,
    )
    parser.add_argument(
        "--green",
        type=int,
        help="The number of acceptable green cubes for each game.",
        default=13,
    )
    parser.add_argument(
        "--blue",
        type=int,
        help="The number of acceptable blue cubes for each game.",
        default=14,
    )

    args = parser.parse_args()

    if args.debug is True:
        logging.basicConfig(level=logging.DEBUG)

    if not args.txt_file.exists() or not args.txt_file.is_file():
        print("Non-existent text file passed, ending program.")
        sys.exit(-1)
    logging.debug("Accepting input from %s", args.txt_file)
    logging.debug(
        "Accepting rgb values of: %s, %s, %s", args.red, args.green, args.blue
    )

    summation = 0
    power_summation = 0
    with open(args.txt_file, "r", encoding="utf-8") as file:
        for line in file:
            game = Game(line)
            if game.is_possible(args.red, args.green, args.blue):
                summation += game.identification

            minimums = game.min_allowed()
            power_summation += minimums[0] * minimums[1] * minimums[2]

    print(f"The resulting summation is {summation}")
    print(f"The resulting power summation is {power_summation}")


if __name__ == "__main__":
    main()
