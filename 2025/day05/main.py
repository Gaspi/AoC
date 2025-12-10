with open('./input.txt', 'r') as file:
    s1, s2 = file.read().split('\n\n')
    fresh = [ [int(c) for c in l.split('-')] for l in s1.split() ]
    ingredients = [ int(i) for i in s2.split() ]

# Quadratic but works in practice
print(sum( any(a <= i <= b for a,b in fresh) for i in ingredients ))

fresh_intervals = []
for a, b in sorted(fresh):
    if fresh_intervals and a <= fresh_intervals[-1][1]+1:
        fresh_intervals[-1][1] = max(b, fresh_intervals[-1][1])
    else:
        fresh_intervals.append( [a, b] )
print( sum(b-a+1 for a,b in fresh_intervals) )
