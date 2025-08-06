import sys
import math
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nv, ne, k = map(int, input().split())
edges = [[] for _ in range(nv+1)]
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    edges[v1].append((v2, cost))
    edges[v2].append((v1, cost))

dist = [[math.inf] * (k+1) for _ in range(nv+1)]
q = []
push(q, (0, 0, 1))
while q:
    cur_cost, cnt, cur = pop(q)
    if dist[cur][cnt] < cur_cost:
        continue
    for nxt, nxt_cost in edges[cur]:
        cost = cur_cost + nxt_cost
        if dist[nxt][cnt] > cost:
            dist[nxt][cnt] = cost
            push(q, (cost, cnt, nxt))
        if cnt < k and dist[nxt][cnt+1] > cur_cost:
            dist[nxt][cnt+1] = cur_cost
            push(q, (cur_cost, cnt+1, nxt))

rst = math.inf
for i in range(k+1):
    rst = min(rst, dist[nv][i])
print(rst)
