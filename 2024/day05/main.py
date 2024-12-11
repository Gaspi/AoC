
rules = []
updates = []
reading_rules = True
with open('./input.txt', 'r') as file:
    for l in file.read().splitlines():
        if l == '':
            reading_rules = False
        else:
            if reading_rules:
                rules.append([int(x) for x in l.split('|')])
            else:
                updates.append([int(x) for x in l.split(',')])

before = {}
for [a,b] in rules:
    if a not in before:
        before[a] = set()
    before[a].add(b)

def is_before(i, j):
    return i in before and j in before[i]


def is_update_sorted(u):
    for i in range(len(u)-1):
        for j in range(i+1, len(u)):
            if is_before(u[j], u[i]):
                return False
    return True


print(sum( u[len(u)//2] for u in updates if is_update_sorted(u)) )


def insert_in_sorted(e, l):
    if l is None:
        return (e, None)
    else:
        (head, tail) = l
        return (e, l) if is_before(e, head) else (head, insert_in_sorted(e, tail))
def sort_update(u):
    res = None
    for e in u:
        res = insert_in_sorted(e, res)
    list_res = []
    while res is not None:
        list_res.append(res[0])
        res = res[1]
    return list_res

incorrect_sorted = [ sort_update(u) for u in updates if not is_update_sorted(u) ]

print( sum( u[len(u)//2] for u in incorrect_sorted) )
