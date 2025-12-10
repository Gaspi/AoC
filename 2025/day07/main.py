with open('./input.txt', 'r') as file:
    data = [
        list(l)
        for l in file.read().splitlines()
    ]

height = len(data)
width = len(data[0])

start = None
for j, c in enumerate(data[0]):
    if c == 'S':
        start = j

res = 0
pos = set([start])
for row in data[1:]:
    npos = set(pos)
    for j in pos:
        if row[j] == '^':
            npos.remove(j)
            npos.add(j-1)
            npos.add(j+1)
            res += 1
    pos = npos


print(res)


memo = {}
def timelines(i, j):
    if (i,j) not in memo:
        memo[(i,j)] = _timelines(i,j)
    return memo[(i,j)]

def _timelines(i, j):
    if j < 0 or j >= width:
        return 0
    elif i == height-1:
        return 1
    elif data[i+1][j] == '^':
        return timelines(i+1, j-1) + timelines(i+1, j+1)
    else:
        return timelines(i+1, j)

print(timelines(0, start))
