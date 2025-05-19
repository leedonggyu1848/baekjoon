import sys
import math
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

n, e = map(int, input().split())

edges = [list() for _ in range(n+1)]

for _ in range(e):
    v1, v2, cost = map(int, input().split())
    edges[v1].append((v2, cost))
    edges[v2].append((v1, cost))

v1, v2 = map(int, input().split())

def dijkstra(start):
    global edges, n
    dist = [math.inf] * (n+1)
    q = []
    dist[start] = 0
    push(q, (0, start))
    while q:
        cur_cost, cur = pop(q)
        if dist[cur] != cur_cost:
            continue
        for edge in edges[cur]:
            nxt, cost = edge
            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                push(q, (dist[cur] + cost, nxt))
    return dist

from_start = dijkstra(1)
from_end = dijkstra(n)
v1_to_v2 = dijkstra(v1)[v2]

last_dist = min(from_start[v1]+from_end[v2], from_start[v2]+from_end[v1])
if last_dist == math.inf or v1_to_v2 == math.inf:
    print(-1)
else:
    print(last_dist + v1_to_v2)
