import sys
import math, heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nv, ne = map(int, input().split())
edges = [[] for _ in range(nv+1)]
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    edges[v1].append((v2, cost))
    edges[v2].append((v1, cost))

pq = []
conn = []
dist = [math.inf] * (nv + 1)
push(pq, (0, 1, 1))
dist[1] = 0
while pq:
    cost, start, bf = pop(pq)
    if dist[start] < cost:
        continue
    if start != bf:
        conn.append((bf, start))
    for nxt, step in edges[start]:
        nxt_cost = cost + step
        if dist[nxt] > nxt_cost:
            dist[nxt] = nxt_cost
            push(pq, (nxt_cost, nxt, start))
print(len(conn))
for v1, v2 in conn:
    print(v1, v2)
