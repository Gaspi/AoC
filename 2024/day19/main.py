with open('./input.txt', 'r') as file:
    lines = file.read().splitlines()
    towels = lines[0].split(', ')
    targets = lines[2:]

def possible(target):
    return target == '' or any(possible(target[len(t):]) for t in towels if target.startswith(t))

print(sum(possible(t) for t in targets))

memo = { '': 1 }
def possibilities(target):
    if target not in memo:
        memo[target] = sum(possibilities(target[len(t):]) for t in towels if target.startswith(t))
    return memo[target]

print(sum(possibilities(t) for t in targets))
