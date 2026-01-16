import sys
from collections import deque
input = sys.stdin.readline

nv, ne = map(int, input().split())
edges = [[] for _ in range(nv+1)]

for _ in range(ne):
    v1, v2 = map(int, input().split())
    edges[v2].append(v1)

rst = 0
start = []
for i in range(nv+1):
    visited = [False] * (nv+1)
    q = deque()
    q.append(i)
    cnt = 1
    visited[i] = True
    while q:
        cur = q.pop()
        for nxt in edges[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                cnt += 1
    if cnt > rst:
        rst = cnt
        start = [i]
    elif cnt == rst:
        start.append(i)

start.sort()
print(*start)
