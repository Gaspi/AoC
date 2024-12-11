
with open('./input_aoc_2024_01.txt', 'r') as file:
    data = [ [int(x) for x in l.split('   ')] for l in file.read().splitlines()]

# Complexity: n.log(n)
left  = sorted([x[0] for x in data])
right = sorted([x[1] for x in data])

# Complexity: n
print( sum( abs(a-b) for (a,b) in zip(left, right) ) )

# Complexity: n²
print( sum(a for a in left for b in right if a == b) )

# Complexity: n.log(n)
from collections import Counter
right_count = Counter(right)
print( sum(a * right_count[a] for a in left) )
