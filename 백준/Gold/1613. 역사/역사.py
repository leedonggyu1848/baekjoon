import sys, math
from collections import deque
input = sys.stdin.readline

nv, ne = map(int, input().split())
indeg = [0] * (nv+1)
edges = [[] for _ in range(nv+1)]
dist = [[math.inf]*(nv+1) for _ in range(nv+1)]

for _ in range(ne):
    s, e = map(int, input().split())
    indeg[e] += 1
    dist[s][e] = 1
for i in range(1, nv+1):
    dist[i][i] = 0

for k in range(1, nv+1):
    for s in range(1, nv+1):
        for e in range(1, nv+1):
            dist[s][e] = min(dist[s][e], dist[s][k] + dist[k][e])

for _ in range(int(input())):
    s, e = map(int, input().split())
    if dist[s][e] != math.inf:
        print(-1)
    elif dist[e][s] != math.inf:
        print(1)
    else:
        print(0)
