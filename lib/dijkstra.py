from collections import deque

n = int(input())
g = []
d = [10**10] * n
d[0] = 0

for i in range(n):
    temp = list(map(int, input().split()))
    k = temp[1]
    temp = temp[2:]
    adj = []
    for j in range(k):
        v, c = temp[j*2], temp[j*2+1]
        adj.append([v, c])
    g.append(adj)

# for i in range(n):
#     print(g[i])

q = deque()
# Add tupple of prev and adj into Queue
q.append((0, g[0]))
done = set()

while q:
    node = q.popleft()
    prev = node[0]
    adj = node[1]
    # print('\nadj:', adj)

    for next in adj:
        v = next[0]
        w = next[1]
        # print('v:', v)
        # print('prev:', prev)

        # d[v] = min(d[v], d[prev] + w)
        if d[prev] + w < d[v]:
            d[v] = d[prev] + w
            # Need to add to Queue regardless of it's in done or not,
            # because the shortest path was updated.
            q.append((v, g[v]))
        if v not in done:
            done.add(v)
            q.append((v, g[v]))

# print('d:', d)

for i in range(len(d)):
    print(i, d[i])



'''
5
0 3 2 3 3 1 1 2
1 2 0 2 3 4
2 3 0 3 3 1 4 1
3 4 2 1 0 1 1 4 4 3
4 2 2 1 3 3
'''