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

def solve_jolt(init_jolt, buttons):
    N = len(init_jolt)
    buttons = set(buttons)

    candidates = [ (0, init_jolt) ]
    while True:
        for i in range(N):
            if all(i not in b for b in buttons):
                candidates = [ c for c in candidates if c[1][i] == 0 ]
        i, b = get_single_buttons(N, buttons)
        if i is not None:
            candidates = [ (score+jolt[i], press(jolt, b, jolt[i])) for score, jolt in candidates ]
            candidates = [ c for c in candidates if all(e >= 0 for e in c[1]) ]
            buttons.remove(b)
            continue
        if len(buttons) == 0:
            return min(c[0] for c in candidates)
        b = sorted(buttons, key=lambda x: ( sum( sum(int(i in b) for b in buttons)==2 for i in x), len(x)), reverse=True)[0]
        candidates = [
            (score+k, press(jolt, b, k))
            for score, jolt in candidates
            for k in range(1+min(jolt[i] for i in b))
        ]
        buttons.remove(b)

for i, (target, buttons, jolt) in enumerate(data):
    print(i, "->", len(buttons), "/",len(jolt))

res = 0
for i, (target, buttons, jolt) in enumerate(data):
    print("##", i, "/", len(data))
    d = solve_jolt(jolt, buttons)
    print(d)
    res += d
print(res)


print("Done.")
