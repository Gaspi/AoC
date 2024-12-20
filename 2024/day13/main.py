import re

with open('./input.txt', 'r') as file:
    lines = file.read().splitlines()
    nbblocks= (len(lines)+1)//4
    data = []
    for i in range(nbblocks):
        buttonA = re.match("Button A: X\+([0-9]+), Y\+([0-9]+)$", lines[4*i])
        buttonB = re.match("Button B: X\+([0-9]+), Y\+([0-9]+)$", lines[4*i+1])
        prize  = re.match("Prize: X=([0-9]+), Y=([0-9]+)$", lines[4*i+2])
        data.append({
            "Ax": int(buttonA[1]),
            "Ay": int(buttonA[2]),
            "Bx": int(buttonB[1]),
            "By": int(buttonB[2]),
            "Px": int(prize[1]),
            "Py": int(prize[2])
            })


def nb_tokens(Ax, Ay, Bx, By, Px, Py):
    tokens = []
    iA = 0
    while True:
        rX = Px - iA * Ax
        rY = Py - iA * Ay
        if rX < 0 or rY < 0:
            return min(tokens) if tokens else 0
        if rX % Bx == 0 and rY % By == 0:
            iB = rX // Bx
            if rY // By == iB:
                tokens.append(3*iA+iB)
        iA+=1

print(sum(nb_tokens(**d) for d in data))

"""
a * Ax + b * Bx = Px
a * Ay + b * By = Py

b * (By.Ax - Bx.Ay) = (Py.Ax - Px.Ay)
"""

def nb_tokens_bis( Ax, Ay, Bx, By, Px, Py):
    Px += 10000000000000
    Py += 10000000000000
    c = By*Ax - Bx*Ay
    if c == 0:
        print("This requires some more work since many solutions exists. Hopefully never happens...")
        print(Ax, Ay, Bx, By, Px, Py)
    else:
        d = Py*Ax - Px*Ay
        if d % c != 0:
            return 0
        b = d // c
        if b < 0:
            return 0
        ap = Px - b*Bx
        if ap < 0 or ap % Ax != 0:
            return 0
        a = ap // Ax
        return 3*a+b

print(sum(nb_tokens_bis(**d) for d in data))
