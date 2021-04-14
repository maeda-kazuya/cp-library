from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.adj = []


q = deque()
q.append(root)

while q:
    node = q.popleft()

    for i in range(len(node.adj)):
        a = node.adj[i]
        q.append(a)