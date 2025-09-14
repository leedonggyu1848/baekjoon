import sys
import heapq, math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nv, ne = map(int, input().split())
edges = [[] for _ in range(nv+1)]
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    edges[v1].append((cost, v2))
    edges[v2].append((cost, v1))

q = []
push(q, (0, 1))
dist = [math.inf] * (nv+1)
prev = [-1 for _ in range(nv+1)]
dist[1] = 0
while q:
    cost, cur = pop(q)
    if cost > dist[cur]:
        continue
    for step, nxt in edges[cur]:
        if dist[nxt] > cost + step:
            prev[nxt] = cur
            dist[nxt] = cost + step
            push(q, (cost + step, nxt))


def dijkstra(v1, v2):
    q = []
    push(q, (0, 1))
    dist = [math.inf] * (nv+1)
    dist[1] = 0
    removed = [(v1, v2), (v2, v1)]
    while q:
        cost, cur = pop(q)
        if cost > dist[cur]:
            continue
        for step, nxt in edges[cur]:
            if (cur, nxt) in removed:
                continue
            if dist[nxt] > cost + step:
                dist[nxt] = cost + step
                push(q, (cost + step, nxt))
    return dist[nv]

answer = dist[nv]
path = set()
p = nv
cur = nv
while cur != -1:
    cur = prev[cur]
    path.add((min(cur, p), max(cur, p)))
    p = cur
for v1, v2 in path:
    answer = max(dijkstra(v1, v2), answer)
print(answer)

