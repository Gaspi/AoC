with open('./input.txt', 'r') as file:
    data = [ [int(x) for x in l if x.isdigit() ] for l in file.read().splitlines()]

print(sum( 10*x[0] + x[-1] for x in data))

with open('./input.txt', 'r') as file:
    data = [ l for l in file.read().splitlines()]

prefixes = [ (str(i), i) for i in range(1,10) ] + [
    ('one', 1),
    ('two', 2),
    ('three', 3),
    ('four', 4),
    ('five', 5),
    ('six', 6),
    ('seven', 7),
    ('eight', 8),
    ('nine', 9),
]

print(prefixes)
def first(s):
    for k,v in prefixes:
        if s.startswith(k):
            return v
    return first(s[1:])

def last(s):
    for k,v in prefixes:
        if s.endswith(k):
            return v
    return last(s[:-1])

print([(l, 10* first(l) + last(l)) for l in data])

print(sum( 10* first(l) + last(l) for l in data))

