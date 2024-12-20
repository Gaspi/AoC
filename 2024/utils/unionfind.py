class UnionFind:
    def __init__(self, keys=[]):
        self.parent = {}
        for k in keys:
            self.add(k)

    def add(self, e):
        if e not in self.parent:
            self.parent[e] = e
    
    def is_root(self, e):
        return self.parent[e] == e
    
    def get_root(self, e):
        self.add(e)
        p = self.parent[e]
        if p == e:
            return e
        else:
            pp = self.parent[p]
            self.parent[e] = pp # Path compression
            return self.get_root(pp)

    def link(self, a, b):
        ra = self.get_root(a)
        rb = self.get_root(b)
        if ra != rb:
            self.parent[ra] = rb

    def __iter__(self):
        return self.parent.__iter__()

    def roots(self):
        return (e for e in self if self.is_root(e))
    
    def copy(self):
        res = UnionFind()
        for k in self.parent:
            res.parent[k] = self.parent[k]
        return res
    
    def get_classes(self):
        root_classes = { r: set() for r in self.roots() }
        class_of = {}
        for e in self.parent:
            r = self.get_root(e)
            root_classes[r].add(e)
            class_of[e] = root_classes[r]
        return (root_classes.values(), class_of)

    def __str__(self):
        return f"UnionFind({len(list(self.roots()))} classes)"

