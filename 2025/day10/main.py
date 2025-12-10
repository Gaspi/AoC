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






print("Done.")
