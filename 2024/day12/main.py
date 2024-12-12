
with open('./input.txt', 'r') as file:
    data = [list(l) for l in file.read().splitlines()]

height = len(data)
width = len(data[0])

parent = { (i,j): (i,j) for i in range(height) for j in range(width) }

def is_root(a):
    return parent[a] == a

def get_root(a):
    b = parent[a]
    if b == a:
        return a
    else:
        # Path compression
        parent[a] = parent[b]
        return get_root(parent[a])

def link(a, b):
    ra = get_root(a)
    rb = get_root(b)
    if a != b:
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


def eval_region(region):
    surface = len(region)
    borders = 0
    for (i,j) in region:
        if i == 0 or (i-1,j) not in region:
            borders += 1
        if i == height or (i+1,j) not in region:
            borders += 1
        if j == 0 or (i,j-1) not in region:
            borders += 1
        if j == width or (i,j+1) not in region:
            borders += 1
    return borders * surface

print(sum(eval_region(r) for r in regions))


def above(p):
    return (p[0]-1,p[1])
def below(p):
    return (p[0]+1,p[1])
def left(p):
    return (p[0],p[1]-1)
def right(p):
    return (p[0],p[1]+1)


def eval_region_bis(region):
    surface = len(region)
    borders = 0
    def border_a(p):
        return p in region and above(p) not in region
    def border_b(p):
        return p in region and below(p) not in region
    def border_l(p):
        return p in region and left(p) not in region
    def border_r(p):
        return p in region and right(p) not in region
    for p in region:
        if border_a(p) and not border_a(right(p)):
            borders += 1
        if border_b(p) and not border_b(right(p)):
            borders += 1
        if border_l(p) and not border_l(below(p)):
            borders += 1
        if border_r(p) and not border_r(below(p)):
            borders += 1
    return borders * surface

print(sum(eval_region_bis(r) for r in regions))
