with open('./input.txt', 'r') as file:
    paper = {
        (i,j): set() # For each paper (i,j), we record its neighbors
        for i,line in enumerate(file.read().split())
        for j,c in enumerate(line)
        if c == '@'
    }

for i in range(height):
    for j in range(height):
        if paper[i][j]:
            for ip in range( max(0, i-1) , min(height, i+2)):
                for jp in range( max(0, j-1) , min( width, j+2) ):
                    if paper[ip][jp]:
                        paper[i][j][2].add(paper[ip][jp])

def is_accessible_paper(i,j):
    return paper[i][j] and sum(
        paper[ip][jp]
        for ip in range( max(0, i-1) , min(height, i+2) )
        for jp in range( max(0, j-1) , min( width, j+2) )
    ) < 5

print(sum(is_accessible_paper(i,j) for i in range(height) for j in range(width)))

tot = 0
while True:
    accessibles = [ (i,j) for i in range(height) for j in range(width) if is_accessible_paper(i, j) ]
    if not accessibles:
        break
    for i, j in accessibles:
        tot += 1
        paper[i][j] = False

print(tot)
