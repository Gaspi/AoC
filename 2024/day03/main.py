
with open('./input.txt', 'r') as file:
    data = file.read()

import re

print( sum(int(r[0]) * int(r[1]) for r in re.findall("mul\(([0-9][0-9]?[0-9]?),([0-9][0-9]?[0-9]?)\)", data) ))

count = 0
do = True
for r in re.findall("mul\(([0-9][0-9]?[0-9]?),([0-9][0-9]?[0-9]?)\)|(do\(\))|(don't\(\))", data):
    if r[2]:
        do = True
    elif r[3]:
        do = False
    elif do:
        count += int(r[0]) * int(r[1])
print(count)
