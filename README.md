# Cube Conundrum
Python implementation of day 2 of [Advent of Code](https://adventofcode.com/2023/day/2) (2023).

## Requirements
* [Python 3.8+](https://www.python.org/)

## Running Instructions
This program can be run with the following command `./main.py [text file] in
which the text file contains a collection of games to parse through for an 
ID and a colleciton of turns.

The default color values can be changed at the command line using the following
syntax: `--{color}={value}`. Without this command, the values will default to 
12 red cubes, 13 green cubes, and 14 blue cubes.

Instructions can be found from the command line by running `./main.py -h`.

## Sample Execution
When this program is run with `./main.py resources/input.txt`, the following 
output is generated: 
```
The resulting summation is 2105
The resulting multiplication is 72422
```

## Prompt Answers
The answer for part one is **2105**.
The answer for part two is **72422**.
