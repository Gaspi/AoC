import re

with open('./input.txt', 'r') as file:
    lines = file.read().splitlines()
    A0 = int(re.match('Register A: (-?[0-9]+)',lines[0])[1])
    B0 = int(re.match('Register B: (-?[0-9]+)',lines[1])[1])
    C0 = int(re.match('Register C: (-?[0-9]+)',lines[2])[1])
    inst = [ int(c) for c in lines[4][9:].split(',') ]

def eval(A0=A0):
    A:int = A0
    B:int = B0
    C:int = C0
    i = 0
    def combo(v) -> int:
        return v if v <= 3 else [A,B,C][v-4]
    while i >= 0 and i < len(inst):
        v = inst[i+1]
        match inst[i]:
            case 0:
                A = A >> combo(v)
            case 1:
                B ^= v
            case 2:
                B = combo(v) % 8
            case 3:
                i = v-2 if A != 0 else i
            case 4:
                B ^= C
            case 5:
                yield combo(v)%8
            case 6:
                B = A >> combo(v)
            case 7:
                C = A >> combo(v)
        i += 2

def pp(l):
    return ','.join( [str(c) for c in l] )

print(pp(eval(A0)))


"""
2,4,
1,3,
7,5,
4,0,
1,3,
0,3,
5,5,
3,0

B=0
C=0
While A > 0 
B = (A % 8 ^ 3)
C = A >> B
print (B^C^3)%8
A = A >> 3

Only the last 8 bit of A are relevant to compute the first printed digit
For the next one, since A is shifted down by 3, the last 11 bits of A are relevant, except for the last 3
And so on

Idea: compute first all possible 8-bits values of A that print out a partial output matching the input instructions
Then for each input A0 that prints out the first n input instructions,
consider, among all the 3-bit extensions of A0, those that print out the first n+1 input instruction
"""


# res[n] has all possible A0 such that eval(A0) return the last n instructions of the program
res = [ set() for _ in range(len(inst)+1) ]

def test(A0):
    e = list(eval(A0))
    if pp(inst).endswith(pp(e)):
        res[len(e)].add(A0)

for A0 in range(256):
    test(A0)
for n in range(1,len(inst)):
    for cur in res[n]:
        for A0 in range(cur << 3, (cur << 3)+8):
            test(A0)

print(res[-1][0])
