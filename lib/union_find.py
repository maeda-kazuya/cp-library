# https://atcoder.jp/contests/atc001/tasks/unionfind_a

class UnionFind:
    def __init__(self, n):
        self.p = [None] * n
        # self.size = []

    def root(self, x):
        if self.p[x] is None:
            return x
        else:
            # 経路圧縮しながらrootを探す
            self.p[x] = self.root(self.p[x])
            return self.p[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        if self.is_same(x, y):
            return
        rootX = self.root(x)
        rootY = self.root(y)
        self.p[rootY] = rootX


n, q = map(int, input().split())
uf = UnionFind(n)

for i in range(q):
    # print('########################')
    # print('i: ', i)
    p, a, b = map(int, input().split())
    # print(a, b)
    if p == 0:
        uf.unite(a, b)
        # print(uf.p)
    else:
        if uf.is_same(a, b):
            print('Yes')
        else:
            print('No')




'''
8 9
0 1 2
0 3 2
1 1 3
1 1 4
0 2 4
1 4 1
0 4 2
0 0 0
1 0 0
'''