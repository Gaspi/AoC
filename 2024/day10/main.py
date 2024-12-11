
with open('./input.txt', 'r') as file:
    data = [ [int(d) for d in line] for line in file.read().splitlines() ]


height = len(data)
width = len(data[0])

pos = [ (i,j) for i in range(height) for j in range(width) ]
alt = { p: data[p[0]][p[1]] for p in pos }
neighbors = { p: set(q for q in pos if abs(p[0]-q[0])+abs(p[1]-q[1]) == 1 and alt[q] == alt[p]+1) for p in pos }

_reachable_nines = {}
def reachable_nines(p):
    if p in _reachable_nines:
        return _reachable_nines[p]
    if alt[p] == 9:
        return set((p,))
    res = set()
    for q in neighbors[p]:
        res |= reachable_nines(q)
    _reachable_nines[p] = res
    return res

print(sum(len(reachable_nines(p)) for p in pos if alt[p] == 0))


_rating = {}
def rating(p):
    if p in _rating:
        return _rating[p]
    if alt[p] == 9:
        return 1
    res = sum(rating(q) for q in neighbors[p])
    _rating[p] = res
    return res

print( sum(rating(p) for p in pos if alt[p] == 0))

