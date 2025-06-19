import sys
import math
input = sys.stdin.readline

nv, ne = map(int, input().split())

nxts = [[-1] * nv for _ in range(nv)]
dist = [[math.inf] * nv for _ in range(nv)]

for i in range(nv):
    dist[i][i] = 0

for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    v1 -= 1
    v2 -= 1
    if dist[v1][v2] > cost:
        dist[v1][v2] = cost
        nxts[v1][v2] = v2

    if dist[v2][v1] > cost:
        dist[v2][v1] = cost
        nxts[v2][v1] = v1


for mid in range(nv):
    for s in range(nv):
        for e in range(nv):
            if dist[s][e] > dist[s][mid] + dist[mid][e]:
                dist[s][e] = dist[s][mid] + dist[mid][e]
                nxts[s][e] = nxts[s][mid]

for y in range(nv):
    for x in range(nv):
        if y == x:
            nxts[y][x] = '-'
        else:
            nxts[y][x] = str(nxts[y][x] + 1)

for nxt in nxts:
    print(' '.join(nxt))
