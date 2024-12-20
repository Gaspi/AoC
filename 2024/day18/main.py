import re

with open('./input.txt', 'r') as file:
    data = [ (int(l.split(',')[0]), int(l.split(',')[1])) for l in file.read().splitlines() ]

print(data)

size = 71
def grid(bytefall):
    grid = [ [ True for _ in range(size)] for _ in range(size) ]
    for i,j in data[:bytefall]:
        grid[i][j] = False
    return grid

def pp(g):
    for i in range(size):
        print(''.join(['.' if g[i][j] else '#' for j in range(size)]))

g = grid(1024)
pp(g)

def solve(grid):
    shortest = [ [ None for _ in range(size)] for _ in range(size) ]
    shortest[0][0] = 0
    pos = set([(0,0)])
    def check(i,j,s):
        if i >= 0 and i < size and j >= 0 and j < size and grid[i][j] and (shortest[i][j] is None or s < shortest[i][j]):
            shortest[i][j] = s
            pos.add((i,j))
    while len(pos):
        i,j = pos.pop()
        s = shortest[i][j]
        check(i-1,j,s+1)
        check(i+1,j,s+1)
        check(i,j-1,s+1)
        check(i,j+1,s+1)
    return shortest[size-1][size-1]

print(solve(g))

i = 1025
j = len(data)
while i < j-1:
    n = (i+j) // 2
    if solve(grid(n)) is None:
        j = n
    else:
        i = n
print(data[i])
