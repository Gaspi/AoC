import re
#from functools import reduce

class Present:
    def __init__(self, block: str):
        lines = block.strip().splitlines()
        self.id = int(lines[0][:-1])
        self.shape = [
                [c == "#" for c in l]
                for l in lines[1:]
            ]
        self.size = sum(int(c) for l in self.shape for c in l)
    def __str__(self):
        return "\n".join(
            [ f"Block #{self.id}:"]+ [
                "".join("#" if c else "." for c in l)
                for l in self.shape
            ]
        )
    def __repr__(self):
        return f"<{self.__str__()}>\n"

class Region:
    def __init__(self, line: str):
        m = re.match("([0-9]+)x([0-9]+): (.*)$", line)
        self.width = int(m[1])
        self.height = int(m[2])
        self.presents = [ int(c) for c in m[3].split(' ') ]
    def __str__(self):
        return f"{self.width}x{self.height}: "+ " ".join(str(c) for c in self.presents)
    def __repr__(self):
        return f"<{self.__str__()}>"


with open('./input.txt', 'r') as file:
    blocks = file.read().split("\n\n")
    regions = [Region(l) for l in blocks[-1].strip().splitlines() ]
    presents = [ Present(b) for b in blocks[:-1] ]







res = 0
for r in regions:
    region_size = r.height*r.width
    presents_size = sum(p*presents[i].size for i,p in enumerate(r.presents))
    if presents_size > region_size:
        continue
    print(region_size, "->", presents_size, ":", region_size-presents_size, "/", region_size/presents_size)
    res += 1

print(res)
print(len(regions))














print("Done.")
