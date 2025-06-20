import sys
import math
input = sys.stdin.readline

nv, ne, query = map(int, input().split())
v_cost = list(enumerate(map(int, input().split())))
dist = [[math.inf] * nv for _ in range(nv)]
max_dog = [[0] *nv for _ in range(nv)]
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    v1 -= 1
    v2 -= 1
    dist[v1][v2] = cost
    dist[v2][v1] = cost
    max_dog[v1][v2] = max(v_cost[v1][1], v_cost[v2][1])
    max_dog[v2][v1] = max(v_cost[v1][1], v_cost[v2][1])

v_cost.sort(key=lambda x:x[1])
for mid, mid_dog in v_cost:
    for start in range(nv):
        for end in range(nv):
            tmp = dist[start][mid] + dist[mid][end]
            dog = max(max_dog[start][mid], max_dog[mid][end], mid_dog)
            if dist[start][end] + max_dog[start][end] > tmp + dog:
                dist[start][end] = tmp
                max_dog[start][end] = dog

for _ in range(query):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    if dist[start][end] == math.inf:
        print('-1')
    else:
        print(dist[start][end] + max_dog[start][end])
