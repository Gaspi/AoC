with open('./input.txt', 'r') as file:
    data = [int(l) for l in file.read().splitlines()]

def next_secret(s):
    s = ((s * 64) ^ s) % 16777216
    s = ((s >> 5) ^ s) % 16777216
    return ((s * 2048) ^ s) % 16777216

def next_n_secret(s, n):
    res = []
    for i in range(n):
        s = next_secret(s)
        res.append(s)
    return res

secrets_series = [ next_n_secret(d, 2000) for d in data ]
print( sum(ss[-1] for ss in secrets_series) )

price_series = [ [ s%10 for s in ss] for ss in secrets_series ]

var_series = [ [None] + [ ps[i+1]-ps[i] for i in range(1999) ] for ps in price_series ]

m = {}
for ps in price_series:
    aux = {}
    for i in range(4,len(ps)):
        seq = (ps[i]-ps[i-1], ps[i-1]-ps[i-2],ps[i-2]-ps[i-3],ps[i-3]-ps[i-4])
        if seq not in aux:
            aux[seq] = ps[i]
    for k,v in aux.items():
        m[k] = m.get(k,0) + v

print(sorted([ (v,k) for k,v in m.items() ], reverse=True)[0])
