import re

data = []
with open('./input.txt', 'r') as file:
    for line in file.read().splitlines():
        data.append([
            c for c in line
            ])


