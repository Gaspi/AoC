
data = []
with open('./input.txt', 'r') as file:
    data = [list(line) for line in file.read().splitlines()]

height = len(data)
width = len(data[0])


obstacles = []
start_x = None
start_y = None
for i,line in enumerate(data):
    for j,c in enumerate(line):
        data[i][j] = c
        if c == '^':
            start_x = i
            start_y = j
        elif c == "#":
            obstacles.append( (i,j) )

rot = {
    (-1, 0): ( 0, 1),
    ( 0, 1): ( 1, 0),
    ( 1, 0): ( 0,-1),
    ( 0,-1): (-1, 0)
}

def play(input_grid):
    grid = [line.copy() for line in input_grid]
    i = start_x
    j = start_y
    v = (-1,0)
    positions = [[ set() for c in line ] for line in input_grid]
    while i >= 0 and i < height and j >= 0 and j < width:
        if grid[i][j] == "#":
            i -= v[0]
            j -= v[1]
            v = rot[v]
        else:
            if v in positions[i][j]:
                return None
            positions[i][j].add(v)
            i += v[0]
            j += v[1]
    return positions

posdir = play(data)
positions = [ (i,j) for i,line in enumerate(posdir) for j,dir in enumerate(line) if dir]

print( len(positions))


loop_pos = []
for p in positions:
    new_data = [line.copy() for line in data]
    if p[0] != start_x or p[1] != start_y:
        new_data[p[0]][p[1]] = "#"
        if play(new_data) is None:
            loop_pos.append(p)
print(len(loop_pos))


