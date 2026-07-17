class UnionFind:
    def __init__(self, n) -> None:
        self.parents = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self, n):
        if self.parents[n] != n:
            self.parents[n] = self.find(self.parents[n])
        return self.parents[n]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parents[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.count -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionGroups = UnionFind(n)

        for x, y in edges:
            unionGroups.union(x, y)

        return unionGroups.count