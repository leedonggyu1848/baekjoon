import sys, math
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nv, ne = map(int, input().split())
w = list(map(int, input().split()))
edges = [[] for _ in range(nv)]
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    v1 -= 1
    v2 -= 1
    edges[v1].append((v2, cost))
    edges[v2].append((v1, cost))

dist = [[math.inf for _ in range(2501)] for _ in range(nv)]
pq = []
pq.append((0, 0, w[0])) # cost, cur_node, min_weight
dist[0][w[0]] = 0
while pq:
    cur_cost, cur, cur_w = pq.pop()
    if dist[cur][cur_w] < cur_cost:
        continue
    for nxt, step in edges[cur]:
        nxt_cost = cur_cost + step*cur_w
        nxt_w = min(cur_w, w[nxt])
        if nxt_cost < dist[nxt][nxt_w]:
            dist[nxt][nxt_w] = nxt_cost
            pq.append((nxt_cost, nxt, nxt_w))

print(min(dist[nv-1]))
