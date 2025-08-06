import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

MAX_N = 4000
nv, ne = map(int, input().split())
fox_edges = [[] for _ in range(MAX_N+1)]
wolf_edges = [[] for _ in range(2*MAX_N+1)]

for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    cost *= 2
    fox_edges[v1].append((v2, cost))
    fox_edges[v2].append((v1, cost))
    wolf_edges[v1].append((v2+MAX_N, cost//2))
    wolf_edges[v2].append((v1+MAX_N, cost//2))
    wolf_edges[v1+MAX_N].append((v2, cost*2))
    wolf_edges[v2+MAX_N].append((v1, cost*2))

fox_dist = [math.inf] * (MAX_N+1)
wolf_dist = [math.inf] * (2*MAX_N+1)

def dijkstra(edges, dist):
    q = []
    push(q, (0, 1))
    dist[1] = 0
    while q:
        cur_cost, cur = pop(q)
        if dist[cur] < cur_cost:
            continue
        for nxt, nxt_cost in edges[cur]:
            cost = cur_cost + nxt_cost
            if cost < dist[nxt]:
                dist[nxt] = cost
                push(q, (cost, nxt))

dijkstra(fox_edges, fox_dist)
dijkstra(wolf_edges, wolf_dist)
rst = 0
for i in range(2, MAX_N+1):
    if fox_dist[i] < min(wolf_dist[i], wolf_dist[i+MAX_N]):
        rst+=1
print(rst)
