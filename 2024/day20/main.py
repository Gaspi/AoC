with open('./input.txt', 'r') as file:
    data = file.read().splitlines()

height = len(data)
width = len(data[0])
all_pos = [(i,j) for i in range(height) for j in range(width)]

start_pos = [(i,j) for i,l in enumerate(data) for j,c in enumerate(l) if c == 'S'][0]
end_pos   = [(i,j) for i,l in enumerate(data) for j,c in enumerate(l) if c == 'E'][0]

wall = [ [ c == '#' for c in l ] for l in data ]
def is_wall(p):
    return wall[p[0]][p[1]]
wall_pos= [p for p in all_pos if is_wall(p)]
open_pos= [p for p in all_pos if not is_wall(p)]

def neighbors(p):
    i,j = p
    if i > 0:
        yield (i-1,j)
    if j > 0:
        yield (i,j-1)
    if i < height-1:
        yield (i+1,j)
    if j < width-1:
        yield (i,j+1)
def open_neighbors(p):
    return (q for q in neighbors(p) if not is_wall(q))

distance_to_start = [ [ None ] * width for _ in range(height) ]
distance_to_end   = [ [ None ] * width for _ in range(height) ]

distance_to_start = { start_pos: 0 }
to_check = set([ (start_pos, 0)] )
while to_check:
    p,d = to_check.pop()
    for q in open_neighbors(p):
        if q not in distance_to_start or d+1 < distance_to_start[q]:
            distance_to_start[q] = d+1
            to_check.add( (q,d+1) )

distance_to_end = { end_pos: 0 }
to_check = set([ (end_pos, 0)] )
while to_check:
    p,d = to_check.pop()
    for q in open_neighbors(p):
        if q not in distance_to_end or d+1 < distance_to_end[q]:
            distance_to_end[q] = d+1
            to_check.add( (q,d+1) )

no_cheat_dst = distance_to_end[start_pos]
print(f"No cheat distance: {no_cheat_dst}")

def get_all_cheats(max_length, minimal_gain):
    for s in open_pos:
        for e in open_pos:
            d = abs(s[0]-e[0]) + abs(s[1]-e[1])
            if d <= max_length:
                gain = no_cheat_dst - (distance_to_start[s] + distance_to_end[e] + d)
                if gain >= minimal_gain:
                    yield (s,e)

print(len(set(get_all_cheats(2, 100))))
print(len(set(get_all_cheats(20, 100))))
