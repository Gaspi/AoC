data = []

with open('./input_small.txt', 'r') as file:
    for l in file.read().splitlines():
        target = None
        buttons = []
        button_masks = []
        jolt = None
        jolt_mask = None
        for e in l.split(' '):
            if e[0] == "[":
                target = tuple(i == "#" for i in e[1:-1])
            elif e[0] == '(':
                button = tuple(int(c) for c in e[1:-1].split(','))
                bmask = tuple(bool(i in button) for i in range(len(target)))
                buttons.append(button)
                button_masks.append(bmask)
            elif e[0] == '{':
                jolt = tuple( int(c) for c in e[1:-1].split(',') )
        data.append( (target, buttons, jolt, button_masks) )


def push(s, b):
    return tuple(c ^ (i in b) for i, c in enumerate(s))

def solve(target, buttons) -> int:
    memo = set()
    mini = 99999999
    stack = [ ( tuple(not c for c in target) , 0, 0) ]
    while stack:
        state, n, i = stack.pop()
        if n >= mini:
            continue
        if all(state):
            mini = n
        else:
            if i < len(buttons):
                b = buttons[i]
                stack.append( (push(state, b), n+1, i+1) )
                stack.append( (         state, n  , i+1) )
    return mini

print(sum(solve(target, buttons) for (target, buttons, jolt, jolt_mask) in data))

import numpy as np
from scipy.optimize import minimize



def solve_bis(jolt, buttons):
    b = np.array(jolt).transpose()
    n = len(b)
    A = np.array([ [ int(i in b) for b in buttons ] for i in range(n) ])
    print(A)
    print(b)
    # Ax = b --> x = [1., -2., 3.]

    fun = lambda x: np.linalg.norm(np.dot(A, x)-b)
    # xo = np.linalg.solve(A,b)
    # sol = minimize(fun, xo, method='SLSQP', constraints={'type': 'ineq', 'fun': lambda x:  x})
    sol = minimize(fun, np.zeros(n), method='L-BFGS-B', bounds=[(0., None) for x in range(n)])

    x = sol['x'] # [2.79149722e-01, 1.02818379e-15, 1.88222298e+00]
    return x

for i,(target, buttons, jolt, buttons_mask) in enumerate(data[:3]):
    print( solve_bis(jolt, buttons))

print("Done.")
