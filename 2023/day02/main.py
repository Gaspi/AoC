import re
import parse
from pathlib import Path

HERE = Path(__file__).resolve().parent

input_file = HERE/ 'input.txt'
input_file = HERE/ 'input2.txt'


def parse_rounds(s):
    res = {'red':0, 'green':0, 'blue': 0}
    for n, c in [e.strip().split(' ') for e in s.split(',')]:
        res[c] = int(n)
    return res

def parse_line(l):
    n, rounds = parse.parse("Game {:n}: {}", l)
    return (n, [ parse_rounds(r) for r in rounds.split(';') ] )

with open(input_file, 'r') as file:
    input_lines = file.read().splitlines()

data = [ parse_line(l) for l in input_lines]



print(
    sum(n
        for n, g in data
        if all(
            r['red'] <= 12 and r['green'] <= 13 and r['blue'] <= 14
            for r in g
            )
    )
)

print( sum(
    max(r['red'] for r in g) * max(r['green'] for r in g) * max(r['blue'] for r in g)
    for _, g in data
))

