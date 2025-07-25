import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]
p = [None for _ in range(n+1)]

depth = [-1] * (n+1)
for _ in range(n-1):
    v1, v2, cost = map(int, input().split())
    edges[v1].append((v2, cost))
    edges[v2].append((v1, cost))

depth[1] = 0
q = deque()
q.appendleft((1,1))
while q:
    cur, d = q.pop()
    for nxt, cost in edges[cur]:
        if depth[nxt] != -1:
            continue
        depth[nxt] = d + 1
        q.appendleft((nxt, d+1))
        p[nxt] = (cur, cost)

for _ in range(int(input())):
    lo, hi = map(int, input().split())
    rst = 0
    if depth[lo] < depth[hi]:
        lo, hi = hi, lo
    while depth[lo] != depth[hi]:
        parent, cost = p[lo]
        lo = parent
        rst += cost
    while lo != hi:
        plo, costlo = p[lo]
        phi, costhi = p[hi]
        rst += costlo + costhi
        lo = plo
        hi = phi
    print(rst)
