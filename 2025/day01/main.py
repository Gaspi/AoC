with open('./input.txt', 'r') as file:
    data = [ ( line[0], int(line[1:]) ) for line in file.read().splitlines() ]


cnt = 0
pos = 50
for rot, n in data:
    pos = (pos + (n if rot == 'R' else -n)) % 100
    if pos == 0:
        cnt += 1
print(cnt)


cnt = 0
pos = 50
for rot, n in data:
    npos = (pos + (n if rot == 'R' else -n)) % 100
    if rot == 'R':
        cnt += (pos + n) // 100
    else:
        cnt += ((100-pos) + n) // 100
        if pos == 0:
            cnt -= 1
    pos = npos
print(cnt)
