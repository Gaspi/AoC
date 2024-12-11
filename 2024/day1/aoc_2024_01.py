
with open('./input_aoc_2024_01.txt', 'r') as file:
    data = [ [int(x) for x in l.split('   ')] for l in file.read().splitlines()]

datal = sorted([x[0] for x in data])
datar = sorted([x[1] for x in data])

print( sum( abs(a-b) for (a,b) in zip(datal, datar) ) )

print( sum(a for a in datal for b in datar if a == b) )
