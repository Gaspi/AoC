

def id_f(x):
    return x

class Grid:
    def __init__(self, data):
        self.grid = [line.copy() for line in data]
        self.height = len(self.grid)
        self.width  = len(self.grid[0])
    
    def copy(self):
        return Grid(self.grid)

    def get(self, p):
        i,j = p
        if i >= 0 and i < self.height and j >= 0 and j < self.width:
            return self.grid[i][j]

    def set(self,p,v):
        i,j = p
        if i >= 0 and i < self.height and j >= 0 and j < self.width:
            self.grid[i][j] = v

    def __iter__(self):
        for i in range(self.height):
            for j in range(self.width):
                yield (i,j)

    def __str__(self,sep=""):
        return "\n".join([sep.join([str(c) for c in l]) for l in self.grid])

