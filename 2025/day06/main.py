import re
from functools import reduce

with open('./input.txt', 'r') as file:
    data = [
        [
            c if c.strip() in ('+', '*') else int(c)
            for c in re.split(r'[\s]+', l)
            if c
        ]
        for l in file.read().splitlines()
    ]
operations = data[-1]
numbers = data[:-1]

print(sum(
    reduce(lambda acc, n: acc * n[i], numbers, 1)
    if op == '*' else
    sum( n[i] for n in numbers)
    for i, op in enumerate(operations)
))


with open('./input.txt', 'r') as file:
    data = list(file)
    operations = data[-1]
    body = data[:-1]
    all_numbers = []
    cur_numbers = []
    for i, o in enumerate(operations):
        if o in ('*', '+'):
            all_numbers.append(cur_numbers)
            cur_numbers = (o, [])
        res = reduce(lambda acc, n: 10*acc+int(n[i]) if n[i] != ' ' else acc, body, 0)
        if res > 0:
            cur_numbers[1].append(res)
    all_numbers.append(cur_numbers)
    all_numbers = all_numbers[1:]

print(sum(
    reduce(lambda acc, n: acc * n, numbers, 1) if op == '*' else sum(numbers)
    for op, numbers in all_numbers
))

