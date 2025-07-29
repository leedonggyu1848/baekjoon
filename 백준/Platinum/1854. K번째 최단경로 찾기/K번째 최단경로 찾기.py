import sys, math
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nv, ne, k = map(int, input().split())
edges = [[] for _ in range(nv+1)]
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    edges[v1].append((v2, cost))

dist = [[] for _ in range(nv+1)]

pq = []
push(pq, (0, 1)) # cost, v
push(dist[1], 0)
while pq:
    cost, cur = pop(pq)
    if len(dist[cur]) >= k and -dist[cur][0] < cost:
        continue
    for edge in edges[cur]:
        nxt, gap = edge
        nxt_cost = cost + gap
        if len(dist[nxt]) >= k and -dist[nxt][0] < nxt_cost:
            continue
        if len(dist[nxt]) >= k:
            pop(dist[nxt])
        push(dist[nxt], -nxt_cost)
        push(pq, (nxt_cost, nxt))

for i in range(1, nv+1):
    if len(dist[i]) != k:
        print(-1)
    else:
        print(-dist[i][0])

