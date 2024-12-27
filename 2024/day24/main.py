import re, random

input_wires = {}
gates = {}
mode_init = True
with open('./input.txt', 'r') as file:
    for line in file.read().splitlines():
        if line == '':
            mode_init = False
        elif mode_init:
            m = re.match('([a-z0-9]{3}): (0|1)', line)
            input_wires[ m[1] ] = int(m[2])
        else:
            m = re.match('([a-z0-9]{3}) (AND|OR|XOR) ([a-z0-9]{3}) -> ([a-z0-9]{3})', line)
            gates[m[4]] = (m[1], m[2], m[3])

output_keys = sorted([k for k in gates if k[0] == 'z'], reverse=True)
def binary_z(z):
    res = 0
    for k in output_keys:
        res = 2*res + z[k]
    return res

def eval(gates, input_wires):
    values = { k: input_wires[k] for k in input_wires }
    def _eval(k):
        if k not in values:
            i1, o, i2 = gates[k]
            values[k] = None # To avoid loop-recomputing it
            v1 = _eval(i1)
            v2 = _eval(i2)
            if v1 is None or v2 is None:
                return None
            values[k] = v1 | v2 if o == 'OR' else v1 & v2 if o == 'AND' else v1 ^ v2
        return values[k]
    return { k: _eval(k) for k in output_keys }

print( binary_z(eval(gates, input_wires)) )

def random_in_out():
    x = random.randrange(0, 2**45)
    y = random.randrange(0, 2**45)
    z = x + y
    vx = { f"x{i:02}" : (x >> i) % 2 for i in range(45) }
    vy = { f"y{i:02}" : (y >> i) % 2 for i in range(45) }
    vz = { f"z{i:02}" : (z >> i) % 2 for i in range(46) }
    return ( dict(**vx, **vy), vz)

def difference(actual_out, expected_out):
    return sum(actual_out[k] != expected_out[k] for k in actual_out)

def flip(gates, x, y):
    return { y if k == x else x if k == y else k: v for k,v in gates.items() }

def score(gates, res_in, res_out):
    eval_out = eval(gates, res_in)
    return 9999 if None in eval_out.values() else difference(eval_out ,res_out)

scores = []
rand_eval = [ random_in_out() for _ in range(10) ]
for x in gates:
    for y in gates:
        if x != y:
            flipped_gates = flip(gates,x, y)
            xy_score = sum( score(flipped_gates, res_in, res_out) for res_in, res_out in rand_eval)
            flip_name = f"{x}<->{y}"
            scores.append( (xy_score, flip_name) )

print(f"No flip:{sum( score(gates, res_in, res_out) for res_in, res_out in rand_eval)}")
for flip_name, flip_score in sorted(scores)[0:10]:
    print(f"{flip_name}: {flip_score}")

# Repeated run of the above show "likely" flips
# Successive best scored flips generate the solution :
gates = flip(gates, 'jbp', 'z35')
gates = flip(gates, 'drg', 'z22')
gates = flip(gates, 'gvw', 'qjb')
gates = flip(gates, 'jgc', 'z15')
print(f"4 flips score:{sum( score(gates, res_in, res_out) for res_in, res_out in rand_eval)}")
