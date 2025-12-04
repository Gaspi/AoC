import re
import parse
from pathlib import Path

HERE = Path(__file__).resolve().parent

input_file = HERE/ 'input.txt'
#input_file = HERE/ 'input2.txt'

with open(input_file, 'r') as file:
    input_lines = file.read().splitlines()

data = input_lines


numbers = []
symbols = set()

for i,l in enumerate(input_lines):
    cur = None
    for j, c in enumerate(l):
        if c.isdigit():
            if cur is None:
                cur = { 'n': 0, 'pos': [] }
                numbers.append(cur)
            cur['n'] = 10*cur['n']+int(c)
            cur['pos'].append((i,j))
        else:
            cur = None
            if c != '.':
                symbols.add((i,j))


def adjacent(p):
    i,j = p
    for di in range(-1, 2):
        for dj in range(-1, 2):
            yield (i+di, j+dj)

def is_adjacent(p, q):
    return abs(p[0]-q[0]) < 2 and abs(p[1]-q[1]) < 2

def is_part(n):
    for p in n['pos']:
        for q in adjacent(p):
            if q in symbols:
                return q
    return None

print(sum(n['n'] for n in numbers if is_part(n)))


res = 0
for i,j in symbols:
    if data[i][j] == "*":
        neighbors = [ n['n'] for n in numbers
            if any( is_adjacent(p, (i,j)) for p in n['pos'])
        ]
        if len(neighbors) == 2:
            res += neighbors[0] * neighbors[1]

print(res)
