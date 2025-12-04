with open('./input.txt', 'r') as file:
    paper = [ [ c == '@' for c in line ] for line in file.read().split() ]
height = len(paper)
width = len(paper[0])

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
