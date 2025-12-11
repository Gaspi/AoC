#import re
#from functools import reduce

data = {}
with open('./input.txt', 'r') as file:
    for l in file.read().splitlines():
        a,b = l.split(':')
        data[a] = b[1:].split(' ')

def path(s):
    if s == 'out':
        return 1
    else:
        return sum( path(i) for i in data[s])

print(path('you'))


memo = {}
def path(p, e, dac, fft):
    if p == e:
        return 1 if dac and fft else 0
    elif (p, dac, fft) in memo:
        return memo[ (p,dac,fft) ]
    else:
        r = sum(path(i, e, dac or p == 'dac', fft or p == 'fft') for i in data[p])
        memo[ (p, dac,fft) ] = r
        return r

print( path('svr', 'out', False, False))

print("Done.")
