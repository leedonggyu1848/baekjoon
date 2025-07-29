import sys, math
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nv, ne, k = map(int, input().split())
edges = [[] for _ in range(nv+1)]
visited = [0] * (nv+1)
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    edges[v1].append([v2, cost, 0])

dist = [-1] * (nv+1)

pq = []
push(pq, (0, 1)) # cost, v
dist[1] = 0
while pq:
    cost, cur = pop(pq)
    if visited[cur] < k:
        visited[cur] += 1
        dist[cur] = max(cost, dist[cur])
    else:
        continue
    for edge in edges[cur]:
        nxt, gap, cnt = edge
        if visited[nxt] < k and cnt < k:
            edge[2] += 1
            push(pq, (cost + gap, nxt))

for i in range(1, nv+1):
    if visited[i] != k:
        print(-1)
    else:
        print(dist[i])

