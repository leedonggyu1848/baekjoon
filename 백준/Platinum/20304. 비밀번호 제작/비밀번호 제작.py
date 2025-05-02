import sys
from collections import deque

maxv = 1_000_000
lim = int(sys.stdin.readline())
m = int(sys.stdin.readline())
tries = [int(t) for t in sys.stdin.readline().split()]
dist = [-1] * (lim+1)

q = deque()
rst = 0
for tri in tries:
    q.append(tri)
    dist[tri] = 0
while q:
    cur = q.popleft()
    for i in range(20):
        mask = 1 << i
        nxt = cur ^ mask
        if nxt > lim or dist[nxt] >= 0:
            continue
        q.append(nxt)
        dist[nxt] = dist[cur] + 1
        rst = max(rst, dist[nxt])

print(rst)
