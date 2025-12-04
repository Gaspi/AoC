
with open('./input.txt', 'r') as file:
    data = [ [ int(c) for c in line ] for line in file.read().split() ]

# Quadratic : works in practice for n=2
print(sum(max(10*c1+c2 for i,c1 in enumerate(l) for c2 in l[i+1:]) for l in data))

# Greedy necessary for n=12
def find_largest(s, n):
    res = 0
    for i in range(n):
        index_min = max(range(len(s) - n + 1 + i), key=lambda i: s[i])
        res = 10*res + s[index_min]
        s = s[index_min+1:]
    return res

print(sum(find_largest(b, 2) for b in data))
print(sum(find_largest(b, 12) for b in data))
