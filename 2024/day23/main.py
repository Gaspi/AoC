with open('./input.txt', 'r') as file:
    data = [l.split('-') for l in file.read().splitlines()]

link = {}
for a,b in data:
    for k in (a,b):
        if k not in link:
            link[k] = set()
    link[a].add(b)
    link[b].add(a)

sols = set()
for a in link:
    if a[0] == 't':
        for b in link[a]:
            for c in link[a]:
                if b in link[c]:
                    sols.add(''.join(sorted([a,b,c])))
print(len(sols))

# Note: this generates cliques with no guarantee to find the biggest one
cliques = []
for k in directly_linked:
    clique = set([k])
    for o in directly_linked:
        if clique.issubset(directly_linked[o]):
            clique.add(o)
    cliques.append(clique)

cliques = sorted(cliques, key=len, reverse=True)
print(','.join(sorted(cliques[0])))
