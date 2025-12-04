# From AoC/2025:
# source .venv/bin/activate

import re
import parse
from pathlib import Path

HERE = Path(__file__).resolve().parent

input_file = HERE/ 'input.txt'
input_file = HERE/ 'input2.txt'

with open(input_file, 'r') as file:
    input_lines = file.read().splitlines()

## If line based input
def parse_line(l):
    n, rounds = parse.parse("Game {:n}: {}", l)
    return (n, rounds.split(';'))

data = [ parse_line(l) for l in input_lines]


## If Grid 
from utils.grid2d import Grid


grid = Grid(input_lines)
for p in grid:
    i,j = p
    grid[p] 

print( list(Coord(1,1).neighbors))