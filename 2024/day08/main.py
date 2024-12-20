

grid = []
with open('./input.txt', 'r') as file:
    grid = [ list(l) for l in file.read().splitlines() ]

height = len(grid)
width = len(grid[0])

antennas = {}
for i,l in enumerate(grid):
    for j,c in enumerate(l):
        if c != '.':
            if c not in antennas:
                antennas[c] = []
            antennas[c].append( (i,j))


antinodes = set()
for freq, positions in antennas.items():
    for p in positions:
        for q in positions:
            if p != q:
                an0 = 2 * q[0] - p[0]
                an1 = 2 * q[1] - p[1]
                if 0 <= an0 < height and 0 <= an1 < width:
                    antinodes.add( (an0, an1) )

print(len(antinodes))

antinodes = set()
for freq, positions in antennas.items():
    for p in positions:
        for q in positions:
            if p != q:
                for i in range(height):
                    for j in range(width):
                        if  (i - p[0]) *  (j - q[1]) == (i-q[0])*(j - p[1]):
                            antinodes.add( (i, j) )

print(len(antinodes))
