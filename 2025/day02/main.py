with open('./input_small.txt', 'r') as file:
    data = [ [ int(c) for c in line.split('-')] for line in file.read().split(',') ]

def invalid(s):
    l = len(s) // 2
    return s[:l] == s[l:]

print(sum(
    n
    for l, u in data
    for n in range(l, u+1)
    if invalid(str(n))
))

def invalid_bis(s):
    l = len(s)
    for d in range(1, 1+(l//2)):
        if l % d == 0:
            splits = [ s[i:i+d] for i in range(0, l, d)]
            if all(s == splits[0] for s in splits[1:]):
                return True
    return False

print(sum(
    n
    for l, u in data
    for n in range(l, u+1)
    if invalid_bis(str(n))
))

