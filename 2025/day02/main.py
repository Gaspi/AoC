with open('./input_small.txt', 'r') as file:
    data = [ [ int(c) for c in line.split('-')] for line in file.read().split(',') ]


def get_invalids(a, b):
    # K = 10**k + 1
    # 10**(k-1) <= n <10**k
    # a <= K * n <= b
    for k in range( len(str(a)) // 2, 9999999):
        K = 10**k + 1
        N_min = (a // K)
        N_max = (b // K)
        if N_min > 10**k:
            continue
        if N_max < 10**(k-1):
            break
        N_max = min(N_max, 10**k-1)
        N_min = max(N_min, 10**(k-1))
        for n in range(N_min, N_max+1):
            m = K*n
            if a <= m <= b:
                yield m

for a,b in data:
    print(list(get_invalids(a, b)))
print(sum(i for a,b in data for i in get_invalids(a, b)))


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

