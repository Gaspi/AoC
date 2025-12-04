
with open('./input.txt', 'r') as file:
    paper = [
        [ int(c) for c in line.split(',') ]
        for line in file.read().split()
    ]



print("Done.")
