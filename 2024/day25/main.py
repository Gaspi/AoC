
keys = []
locks = []
with open('./input.txt', 'r') as file:
    lines = file.read().splitlines()
for i in range(0, len(lines), 8):
    h = [0,0,0,0,0]
    for l in lines[i+1:i+6]:
        for j,c in enumerate(l):
            h[j] += (c == '#')
    if lines[i] == '.....':
        keys.append(h)
    else:
        locks.append(h)

print( sum( all((k[i]+l[i] <= 5) for i in range(5)) for k in keys for l in locks ))
