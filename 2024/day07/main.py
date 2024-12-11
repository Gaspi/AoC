
data = []
with open('./input.txt', 'r') as file:
    for l in file.read().splitlines():
        total, args = l.split(': ')
        data.append((int(total), [int(a) for a in args.split(' ')]))


def possible(target, args):
    partials = set([args[0]])
    for n in args[1:]:
        partials = set([p+n for p in partials]+[p*n for p in partials])
    return target in partials

print( sum(total for (total, args) in data if possible(total, args)))


def possible2(target, args):
    partials = set([args[0]])
    for n in args[1:]:
        new_partials = [p+n for p in partials]+[p*n for p in partials] + [ int(str(p)+str(n)) for p in partials]
        partials = set([p for p in new_partials if p <= target] )
    return target in partials

print( sum(total for (total, args) in data if possible2(total, args)))
