
with open('./input.txt', 'r') as file:
    data = [list(l) for l in file.read().splitlines()]

height = len(data)
width = len(data[0])

def above(p):
    return (p[0]-1,p[1])
def below(p):
    return (p[0]+1,p[1])
def left(p):
    return (p[0],p[1]-1)
def right(p):
    return (p[0],p[1]+1)


parent = { (i,j): (i,j) for i in range(height) for j in range(width) }

def get_root(a):
    b = parent[a]
    if b == a:
        return a
    else:
        parent[a] = parent[b] # Path compression
        return get_root(parent[a])

def link(a, b):
    ra = get_root(a)
    rb = get_root(b)
    if ra != rb:
        parent[ra] = rb

for i in range(height):
    for j in range(width):
        if i > 0 and data[i-1][j] == data[i][j]:
            link((i-1,j), (i,j))
        if j > 0 and data[i][j-1] == data[i][j]:
            link((i,j-1), (i,j))

regions_map = {}
for i in range(height):
    for j in range(width):
        r = get_root((i,j))
        if r not in regions_map:
            regions_map[r] = set()
        regions_map[r].add((i,j))
regions = regions_map.values()

print(f"Found {len(regions)} regions")

def border_above(region, p):
    return p in region and above(p) not in region
def border_below(region, p):
    return p in region and below(p) not in region
def border_left(region, p):
    return p in region and left(p) not in region
def border_right(region, p):
    return p in region and right(p) not in region
def nb_borders(region, p):
    return border_above(region, p) + border_below(region, p) + border_left(region, p) + border_right(region, p)

def eval_region(region):
    return len(region) * sum(nb_borders(region, p) for p in region)

print(sum(eval_region(r) for r in regions))


def nb_bulk_borders(region, p):
    return sum((
        border_above(region, p) and not border_above(region, right(p)),
        border_below(region, p) and not border_below(region, right(p)),
        border_left( region, p) and not border_left( region, below(p)),
        border_right(region, p) and not border_right(region, below(p)),
    ))

def eval_region_bis(region):
    return len(region) * sum(nb_bulk_borders(region, p) for p in region)

print(sum(eval_region_bis(r) for r in regions))
