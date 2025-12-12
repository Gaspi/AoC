data = []

with open('./input.txt', 'r') as file:
    for l in file.read().splitlines():
        target = None
        buttons = []
        jolt = None
        for e in l.split(' '):
            if e[0] == "[":
                target = tuple(i == "#" for i in e[1:-1])
            elif e[0] == '(':
                buttons.append( tuple(int(c) for c in e[1:-1].split(',')) )
            elif e[0] == '{':
                jolt = tuple( int(c) for c in e[1:-1].split(',') )
        data.append( (target, buttons, jolt) )


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

print(sum(solve(target, buttons) for (target, buttons, jolt) in data))



def get_actions(buttons):
    N = max(i for button in buttons for i in button)+1
    button_set = set(buttons)
    checked = [False for i in range(N)]
    for i in sorted(range(N), key=lambda i:sum( int(i in b) for b in buttons) ):
        candidates = [b for b in button_set if i in b]
        for button in candidates:
            button_set.remove(button)
            to_set = []
            for k in button:
                if not checked[k]:
                    a = [b for b in button_set if k in b]
                    if len(a) == 0:
                        to_check.append(k)
                        checked[k] = True
                    if len(a) == 1:
                        to_set.append( (k, a[0]) )
            yield (button, to_set, to_check)



def press_all(jolt, button):
    N = len(jolt)
    maxi = min(jolt[i] for i in button)
    for k in range(maxi+1):
        yield (k, tuple( jolt[i] - k * int(i in button) for i in range(N)))


def press(jolt, button, k):
    return tuple(j - k * int(i in button) for i,j in enumerate(jolt))

def get_single_buttons(N, buttons):
    for i in range(N):
        s = [b for b in buttons if i in b]
        if len(s) == 1:
            return (i, s[0])
    return (None, None)


class Button:
    def __init__(self, press, effect):
        self.press = press
        self.effect = effect
    def minus(self):
        self.press = [ -pre for pre in self.press]
        self.effect = [ -eff for eff in self.effect]
    def is_pivot(self, i):
        if self.effect[i] < 0:
            self.minus()
        return self.effect[i]
    def pivot(self, i, b):
        if self.effect[i] != 0:
            c = self.effect[i] // b.effect[i]
            self.effect = [ (e - c*be) for e, be in zip(self.effect, b.effect) ]
            self.press  = [ (p - c*bp) for p, bp in zip(self.press, b.press) ]
    def add(self, b):
        self.effect = [ e + be for e, be in zip(self.effect, b.effect) ]
        self.press  = [ p + bp for p, bp in zip(self.press, b.press) ]
    def sub(self, b):
        self.effect = [ e - be for e, be in zip(self.effect, b.effect) ]
        self.press  = [ p - bp for p, bp in zip(self.press, b.press) ]
    def __str__(self):
        return ",".join([ str(e) for e in self.effect]) + " / " + \
            ",".join([ str(e) for e in self.press])

def list_add(a,b):
    return [ c+d for c,d in zip(a,b)]
def list_times(a,n):
    return [ c*n for c in a]

import math
math.gcd

def solve_jolt(target, buttons):
    target = [e for e in target]
    N = len(target)
    nb_buttons = len(buttons)
    print(N, nb_buttons)
    buttons = set(
        Button(
            press= [int(j==i) for j in range(nb_buttons)], # Pressing these buttons
            effect= [ int(j in b) for j in range(N) ]       # Has that effect on joltage
        )
        for i,b in enumerate(buttons)
    )
    done = set()
    pressed = [0 for j in range(nb_buttons)]
    while any(e != 0 for e in target):
        #print(pressed)
        #print(target)
        #for b in buttons:
        #    print(b)
        i,e = [ (i,e) for i,e in enumerate(target) if e != 0][0]
        pivots = [b for b in buttons if b.is_pivot(i)]
        g = abs(math.gcd(*[p.effect[i] for p in pivots]))
        if e % g != 0:
            print("!!! Issue !!!")
            print()
            print()
            print(e, g)
        if not pivots:
            print("Failed to pivot:")
            for b in buttons:
                if abs(b.effect[i]) != 0:
                    print(" ",b)
            return 0
        while all(p.effect[i] > g for p in pivots):
            p1 = sorted(pivots, key=lambda p: p.effect[i], reverse=True)[0]
            p2 = sorted(pivots, key=lambda p: p.effect[i])[0]
            p1.sub(p2)
        p = [p for p in pivots if p.effect[i] == g][0]
        n = e // g
        for j, press in enumerate(p.press):
            pressed[j] += n * press
        for j, effect in enumerate(p.effect):
            target[j] -= n * effect
        done.add(p)
        buttons.remove(p)
        for b in buttons:
            b.pivot(i, p)
    
    res = 99999999
    buttons = [ b for b in buttons if all(e == 0 for e in b.effect) ]
    print("Remain:", len(buttons))
    # Very ugly : we try all combinations of the remaining buttons within a (multi-)range
    for indices in multi_range(-60, 60, [], len(buttons)):
        p = pressed
        t = target
        for b,n in zip(buttons,indices):
            p = list_add(p, list_times(b.press, n))
            t = list_add(t, list_times(b.effect, n))
        if all(pi >= 0 for pi in p):
            res = min(res, sum(p))
    if res == 99999999:
        print("some work...")
        for indices in multi_range(-120, 120, [], len(buttons)):
            p = pressed
            t = target
            for b,n in zip(buttons,indices):
                p = list_add(p, list_times(b.press, n))
                t = list_add(t, list_times(b.effect, n))
            if all(pi >= 0 for pi in p):
                res = min(res, sum(p))
    if res == 99999999:
        print("hardcore")
        print(pressed)
        print(target)
        for b in buttons:
            print(b)
        for indices in multi_range(-500, 500, [], len(buttons)):
            p = pressed
            t = target
            for b,n in zip(buttons,indices):
                p = list_add(p, list_times(b.press, n))
                t = list_add(t, list_times(b.effect, n))
            if all(pi >= 0 for pi in p):
                res = min(res, sum(p))
    if res == 99999999:
        print(pressed)
        print(target)
        for b in buttons:
            print(b)
    return res

def multi_range(mini, maxi, acc, n):
    if n == 0:
        yield acc
    else:
        for i in range(mini, maxi):
            yield from multi_range(mini, maxi, acc+[i], n-1)




res = 0
for i, (target, buttons, jolt) in enumerate(data):
    print("##", i, "/", len(data))
    d = solve_jolt(jolt, buttons)
    print(d)
    res += d
print(res)


# 17820

print("Done.")
