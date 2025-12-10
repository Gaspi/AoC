#import re
#from functools import reduce

data = []

with open('./input_small.txt', 'r') as file:
    for l in file.read().splitlines():
        target = None
        buttons = []
        req = []
        for e in l.split(' '):
            if e[0] == "[":
                target = tuple(i == "#" for i in e[1:-1])
            elif e[0] == '(':
                buttons.append( tuple( int(c) for c in e[1:-1].split(',')) )
            elif e[0] == '{':
                req.append( tuple( int(c) for c in e[1:-1].split(',')) )
        data.append( (target, buttons, req) )

print(data)

def pp(s):
    return ''.join('#' if c else "." for c in s)

def solve(target, buttons) -> int:
    print("Start", pp(target), buttons )
    memo = set()
    mini = 99999999
    stack = [ ( tuple(not c for c in target) , 0) ]
    while stack:
        state,n = stack.pop()
        print("->", pp(state), n )
        if n >= mini or state in memo:
            continue
        memo.add(state)
        if all(state):
            mini = n
        else:
            for b in buttons:
                stack.append( (tuple(c ^ (i in b) for i,c in enumerate(state)), n+1) )
                print( pp(tuple(c ^ (i in b) for i,c in enumerate(state))), n+1, b )
    print(mini)
    return mini




print(sum(solve(target, buttons) for (target, buttons, req) in data))

print("Done.")
