
with open('./input.txt', 'r') as file:
    data = [ [int(c) for c in l.split(' ')] for l in  file.read().splitlines()]

def safe(seq):
    var = (1,2,3) if seq[1] > seq[0] else (-1,-2,-3) if seq[0] > seq[1] else ()
    return all(seq[i+1]-seq[i] in var for i in range(len(seq)-1))

print(sum(safe(u) for u in data))

def safe_x(seq):
    return any( safe(seq[:i]+seq[i+1:]) for i in range(len(seq)))

print(sum(safe_x(u) for u in data))
