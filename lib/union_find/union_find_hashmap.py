# https://leetcode.com/problems/redundant-connection/

class DisjointSet:
    def __init__(self):
        self.p = {}

    def root(self, x):
        if x not in self.p:
            return x
        else:
            # 経路圧縮しながらrootを探す
            self.p[x] = self.root(self.p[x])
            return self.p[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        if self.is_same(x, y):
            return False
        rootX = self.root(x)
        rootY = self.root(y)
        self.p[rootY] = rootX

        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        uf = DisjointSet()

        for edge in edges:
            org, dst = edge[0], edge[1]

            if not uf.unite(org, dst):
                return edge