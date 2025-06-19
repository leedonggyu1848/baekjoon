import sys
import math
input = sys.stdin.readline

nv, ne = map(int, input().split())
dists = [[math.inf]*(nv+1) for _ in range(nv+1)]

for i in range(1, nv+1):
    dists[i][i] = 0

for _ in range(ne):
    s, e, cost = map(int, input().split())
    dists[s][e] = cost

k = int(input())
starts = list(map(int, input().split()))

for mid in range(1, nv+1):
    for s in range(1, nv+1):
        for e in range(1, nv+1):
            tmp = dists[s][mid] + dists[mid][e]
            if tmp < dists[s][e]:
                dists[s][e] = tmp

minv = math.inf
rst = []
for end in range(1, nv+1):
    cur = 0
    for start in starts:
        cur = max(cur, dists[start][end] + dists[end][start])
    if minv > cur:
        minv = cur
        rst = [end]
    elif minv == cur:
        rst.append(end)
rst.sort()
print(' '.join(map(str, rst)))
