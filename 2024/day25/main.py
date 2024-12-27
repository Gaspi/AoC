
with open('./input.txt', 'r') as file:
    lines = file.read().splitlines()
keys = []
locks = []
for i in range(0, len(lines), 8):
    heights = [0,0,0,0,0]
    for l in lines[i+1:i+6]:
        for j,c in enumerate(l):
            heights[j] += (c == '#')
    (keys if lines[i] == '.....' else locks).append(heights)

print(sum( all(k[i]+l[i] <= 5 for i in range(5)) for k in keys for l in locks))
