data = []

with open('./input.txt', 'r') as file:
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



def get_actions(buttons):
    N = max(i for button in buttons for i in button)+1
    button_set = set(buttons)
    checked = [False for i in range(N)]
    for i in sorted(range(N), key=lambda i:sum( int(i in b) for b in buttons) ):
        candidates = [b for b in button_set if i in b]
        for button in candidates:
            button_set.remove(button)
            to_check = []
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



def press(jolt, button, k):
    return tuple(j - k * int(i in button) for i,j in enumerate(jolt))

def press_all(jolt, button):
    N = len(jolt)
    maxi = min(jolt[i] for i in button)
    for k in range(maxi+1):
        yield (k, tuple( jolt[i] - k * int(i in button) for i in range(N)))

res = 0
for i,(target, buttons, jolt, buttons_mask) in enumerate(data):
    print("##", i, "/", len(data))
    candidates = [ (0, jolt) ]
    for button, index_to_check in get_actions(buttons):
        print(len(candidates))
        candidates = [
            (cnt+k, njolt)
            for (cnt, jolt) in candidates
            for (k, njolt) in press_all(jolt, button)
            if all(njolt[i] == 0 for i in index_to_check)
            ]
    m = min(c for c, j in candidates)
    # print(m)
    res += m

print(res)

print("Done.")
