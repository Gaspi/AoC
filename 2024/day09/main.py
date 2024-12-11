
with open('./input.txt', 'r') as file:
    data = [ int(d) for d in file.read().splitlines()[0] ]

blocks = []
b = True
i = 0
for d in data:
    blocks.extend([i if b else None]*d)
    i+=b
    b = not b

compact = blocks.copy()
i=0
j=len(compact)-1
while i < j:
    if compact[i] != None:
        i += 1
    elif compact[j] == None:
        j -= 1
    else:
        compact[i] = compact[j]
        compact[j] = None
        i += 1
        j -= 1

print( sum( i * v for i, v in enumerate(compact) if v != None ))


n = 0
blocks = []
holes = []
for i,d in enumerate(data):
    if i%2 == 0:
        blocks.append({"pos":n, "size":d})
    elif d > 0:
        holes.append({"pos":n,"size":d})
    n += d

for block in reversed(blocks):
    for hole in holes:
        if hole['pos'] < block['pos'] and hole['size'] >= block['size']:
            block['pos'] = hole['pos']
            hole['pos'] += block['size']
            hole['size'] -= block['size']


print(sum( sum( (b["pos"]+j) * i for j in range(b["size"])) for i,b in enumerate(blocks)))
