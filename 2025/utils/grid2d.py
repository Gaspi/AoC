from typing import Iterable, TypeVar, Generic, Self, Iterator

class Coord:
    i: int
    j: int
    def __init__(self, i: int, j:int):
        self.i = i
        self.j = j

    @property
    def x(self):
        return self.i
    @x.setter
    def x(self, value):
        self.i = value

    @property
    def y(self):
        return self.j
    @y.setter
    def y(self, value):
        self.j = value

    def __eq__(self, c) -> bool:
        return self.i == c.i and self.j == c.j

    def __iter__(self):
        yield self.i
        yield self.j

    def __getitem__(self, index: 0|1) -> int:
        return self.j if index else self.i

    def __repr__(self) -> str:
        return f"Coord({self.i}, {self.j})"

    def __str__(self) -> str:
        return f"Coord({self.i}, {self.j})"

    def distance(self, p: Self) -> int:
        return abs(self.i-p.i) + abs(self.j-p.j)

    def neighbors(self) -> Iterator[Self]:
        for di in range(-1,2):
            for dj in range(-1, 2):
                yield Coord(self.i+di, self.j+dj)

    def strict_neighbors(self) -> Iterator[Self]:
        for c in self.neighbors():
            if c != self:
                yield c

    def is_neighbor(self, p: Self) -> bool:
        return abs(self.i-p.i) <= 1 and abs(self.j-p.j) <= 1
    
    def adjacents(self) -> Iterator[Self]:
        yield Coord(self.i+1, self.j  )
        yield Coord(self.i-1, self.j  )
        yield Coord(self.i  , self.j+1)
        yield Coord(self.i  , self.j-1)

    def is_adjacent(self, p: Self) -> bool:
        return self.distance(p) <= 1

T = TypeVar("T")


class Grid(Generic[T]):
    grid: list[list[T]]
    height: int
    width: int

    def __init__(self, data: Iterable[Iterable[T]]):
        self.grid = [ [ c for c in line ] for line in data]
        self.height = len(self.grid)
        self.width  = len(self.grid[0])
    
    def copy(self) -> Self:
        return Grid(self.grid)

    def __getitem__(self, p: Coord|tuple[int,int]) -> T:
        i,j = p
        if i >= 0 and i < self.height and j >= 0 and j < self.width:
            return self.grid[i][j]

    def __setitem__(self, p: Coord|tuple[int,int], v: T) -> None:
        i,j = p
        if i >= 0 and i < self.height and j >= 0 and j < self.width:
            self.grid[i][j] = v

    def __iter__(self):
        for i in range(self.height):
            for j in range(self.width):
                yield (i,j)

    def __str__(self,sep=""):
        return "\n".join([sep.join([str(c) for c in l]) for l in self.grid])
