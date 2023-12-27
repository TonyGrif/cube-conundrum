#!/usr/bin/env python3

"""This module contains the main driver of the Cube Conundrum project.
"""


import argparse
import logging
import sys
from pathlib import Path


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

    args = parser.parse_args()

    if args.debug is True:
        logging.basicConfig(level=logging.DEBUG)

    if not args.txt_file.exists() or not args.txt_file.is_file():
        print("Non-existent text file passed, ending program.")
        sys.exit(-1)


if __name__ == "__main__":
    main()
