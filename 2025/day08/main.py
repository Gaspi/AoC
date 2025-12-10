from unionfind import UnionFind

with open('./input.txt', 'r') as file:
    data = [ tuple(int(c) for c in l.split(',')) for l in file.read().splitlines() ]


def dst(a, b):
    return sum((ai-bi)**2 for ai, bi in zip(a,b))

junctions = sorted(
    (dst(a,b), a, b)
    for i, a in enumerate(data)
    for b in data[i+1:]
)

print("Ready")

circuits = UnionFind(keys=data)
for _,a,b in junctions[:1000]:
    circuits.link(a,b)

classes, _ = circuits.get_classes()
a,b,c = list(sorted([ len(x) for x in classes], reverse=True))[:3]
print(a*b*c)


circuits = UnionFind(keys=data)
for _,a,b in junctions:
    circuits.link(a,b)
    if len(circuits.roots) == 1:
        print(a[0] * b[0])
        break
