
with open('./input.txt', 'r') as file:
    data = [ list(l) for l in file.read().splitlines()]

height = len(data)
width = len(data[0])

def get(i,j):
    if 0 <= i < height and 0 <= j < width:
        return data[i][j]

def search(i,j):
    res = 0
    if data[i][j] == 'X':
        for vx in range(-1,2):
            for vy in range(-1,2):
                if not vx == vy == 0 and all([get(i+k*vx,j+k*vy) == 'XMAS'[k] for k in range(1,4)]):
                    res += 1
    return res

print(sum(search(i,j) for i in range(height) for j in range(width)))

def search_x(i,j):
    if data[i][j] == 'A':
        around = data[i+1][j+1]+data[i+1][j-1]+data[i-1][j-1]+data[i-1][j+1]
        return around in ['MMSS', 'MSSM', 'SSMM', 'SMMS']
    else:
        return False

print(sum(search_x(i,j) for i in range(1, height-1) for j in range(1, width-1)))
