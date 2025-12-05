with open('./input.txt', 'r') as file:
    s1, s2 = file.read().split('\n\n')
    fresh = [ [int(c) for c in l.split('-')] for l in s1.split() ]
    ingredients = [ int(i) for i in s2.split() ]

with open('./input.txt', 'r') as file:
    data = [ [int(c) for c in l.split(',')] for l in file.read().split() ]


print('Done.')
