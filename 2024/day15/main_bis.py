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

grid = [
    list(l.replace('#','##').replace('.','..').replace('@','@.').replace('O','[]'))
    for l in data]
height = len(grid)
width = len(grid[0])

def print_grid(grid):
    for l in grid:
        print(''.join(l))


def move(pos, direction):
    global grid
    vi = { '^': -1, 'v':1 }.get(direction, 0)
    vj = { '<': -1, '>':1 }.get(direction, 0)
    n = 1
    ok_to_move= set()
    check_to_move = set([pos])
    while check_to_move:
        (i,j) = check_to_move.pop()
        if grid[i][j] == "#":
            return pos
        if grid[i][j] == "." or (i,j) in ok_to_move:
            continue
        ok_to_move.add((i,j))
        check_to_move.add((i+vi, j+vj))
        if grid[i][j] == "[":
            check_to_move.add((i, j+1))
        if grid[i][j] == "]":
            check_to_move.add((i, j-1))
    new_grid = [ l.copy() for l in grid]
    for i,j in ok_to_move:
        new_grid[i][j] = "."
    for i,j in ok_to_move:
        new_grid[i+vi][j+vj] = grid[i][j]
    grid = new_grid
    return (pos[0]+vi, pos[1]+vj)



pos = [(i,j) for i in range(height) for j in range(width) if grid[i][j] == '@'][0]
for direction in moves:
    pos = move(pos, direction)
    #print(f"Move: {direction}")
    #print_grid(grid)
    #print()

#print_grid(grid)
print(sum(100*i+j for i in range(height) for j in range(width) if grid[i][j] == '['))
