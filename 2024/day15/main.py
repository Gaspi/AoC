import re

data = []
gridmode = True
moves = []
with open('./input.txt', 'r') as file:
    for line in file.read().splitlines():
        if line == '':
            gridmode = False
        else:
            if gridmode:
                data.append(line)
            else:
                for c in line:
                    moves.append(c)


grid = [list(l) for l in data]
height = len(grid)
width = len(grid[0])

def move(pos, direction):
    i,j = pos
    vi = { '^': -1, 'v':1 }.get(direction, 0)
    vj = { '<': -1, '>':1 }.get(direction, 0)
    n = 1
    while grid[i+n*vi][j+n*vj] == 'O':
        n += 1
    if grid[i+n*vi][j+n*vj] != '.': 
        return pos
    grid[i][j] = '.'
    grid[i+vi][j+vj] = '@'
    if n > 1:
        grid[i+n*vi][j+n*vj] = 'O'
    return (i+vi, j+vj)

def print_grid(grid):
    for l in grid:
        print(''.join(l))


#print_grid(grid)

pos = [(i,j) for i in range(height) for j in range(width) if grid[i][j] == '@'][0]
for direction in moves:
    pos = move(pos, direction)
    #print(f"Move: {direction}")
    #print_grid(grid)
    #print()

print(sum(100*i+j for i in range(height) for j in range(width) if grid[i][j] == 'O'))
