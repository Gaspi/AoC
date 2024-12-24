import sys
import re

sys.path.insert(0,'..')
from utils.grid2d import *
from utils.unionfind import *

#uf = UnionFind()
#uf.link(a, b)
#...
#all_classes, class_of = uf.get_classes()

cur_input = []
inputs = [cur_input]
with open('./input.txt', 'r') as file:
    for line in file.read().splitlines():
        if line:
            cur_input.append(line)
        else:
            cur_input = []
            inputs.append(cur_input)

grid = Grid([
    [
        c != '#'
        for c in line
    ]
    for line in inputs[0]
])

iS,jS = [ (i,j) for i,line in enumerate(inputs[0]) for j,c in enumerate(line)  if c == 'S' ][0]
iE,jE = [ (i,j) for i,line in enumerate(inputs[0]) for j,c in enumerate(line)  if c == 'E' ][0]

print(grid)
print(iS,jS)
print(iE,jE)


big_int = 9999999999999
scores = [
    [
        [big_int,big_int,big_int,big_int]
        for j in range(grid.width)
    ]
    for i in range(grid.height)
]

from sortedcontainers import SortedList

# Directions :
# 0 : East
# 1 : South
# 2 : West
# 3 : North

search_pos = SortedList(key=lambda x:-x[3])
search_pos.add((iS,jS,0,0,[]))
min_score = big_int

paths = set([(iS,jS),(iE,jE)])

n = 0
while len(search_pos) > 0:
    i,j,d,s,steps = search_pos.pop()
    nsteps = steps + [(i,j)]
    #print(i,j,d,s, len(search_pos))

    if (i,j) == (iE,jE):
        if s <= min_score:
            if s < min_score:
                paths = set([(iS,jS),(iE,jE)])
                min_score = s
            for c in steps:
                paths.add(c)
            print(s, len(paths))
    if s >= min_score or s > scores[i][j][d]:
        continue
    scores[i][j][d] = s
    if s + 1000 < min_score:
        search_pos.add( (i,j,(d+1)%4, s+1000,nsteps))
        search_pos.add( (i,j,(d-1)%4, s+1000,nsteps))
    ip = i+(1 if d == 1 else -1 if d == 3 else 0)
    jp = j+(1 if d == 0 else -1 if d == 2 else 0)
    if grid.get((ip,jp)):
        search_pos.add( (ip,jp,d, s+1,nsteps))

print(min_score)

print(len(paths))
