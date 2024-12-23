with open('./input.txt', 'r') as file:
    data = file.read().splitlines()

def above(p):
    return (p[0]-1,p[1])
def below(p):
    return (p[0]+1,p[1])
def left(p):
    return (p[0],p[1]-1)
def right(p):
    return (p[0],p[1]+1)

pos = {
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),
    '0': (3,1),
    'A': (3,2),
    '^': (3,1),
    '<': (4,0),
    'v': (4,1),
    '>': (4,2)
}

forbidden_position = (3,0)

def shortest_move_seq_pos(p, q):
    if p == q:
        return ['A']
    res = []
    if p[0] < q[0] and below(p) != forbidden_position:
        res += [ 'v'+c for c in shortest_move_seq_pos(below(p), q) ]
    if p[0] > q[0] and above(p) != forbidden_position:
        res += [ '^'+c for c in shortest_move_seq_pos(above(p), q) ]
    if p[1] < q[1]:
        res += [ '>'+c for c in shortest_move_seq_pos(right(p), q) ]
    if p[1] > q[1] and left(p) != forbidden_position:
        res += [ '<'+c for c in shortest_move_seq_pos(left(p), q) ]
    return res

def shortest_move_seq(start, end):
    return shortest_move_seq_pos(pos[start], pos[end])


memo = {}
def nb_moves_to_transition(start, end, steps):
    if steps == 0:
        return 1
    else:
        if (start, end, steps) not in memo:
            memo[(start, end, steps)] = min(
                [
                    nb_moves_to_sequence(seq, steps-1)
                    for seq in shortest_move_seq(start, end)
                ]
            )
        return memo[(start, end, steps)]

def nb_moves_to_sequence(seq, steps):
    return sum(
        nb_moves_to_transition('A' if i == 0 else seq[i-1], seq[i], steps)
        for i in range(len(seq))
    )

print(nb_moves_to_sequence('029A', 1))
print(nb_moves_to_sequence('029A', 2))
print(nb_moves_to_sequence('029A', 3))
print(sum( nb_moves_to_sequence(d,  3)*int(d[:-1]) for d in data))
print(sum( nb_moves_to_sequence(d, 26)*int(d[:-1]) for d in data))
