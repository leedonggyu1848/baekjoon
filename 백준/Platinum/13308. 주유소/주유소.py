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

dist = [{} for _ in range(nv)]
pq = []
push(pq,(0, w[0], 0)) # cost, min_weight, cur_node
dist[0][w[0]] = 0
while pq:
    cur_cost, cur_w, cur = pop(pq)
    if cur == nv-1:
        print(cur_cost)
        break
    if dist[cur][cur_w] < cur_cost:
        continue
    for nxt, step in edges[cur]:
        nxt_cost = cur_cost + step*cur_w
        nxt_w = min(cur_w, w[nxt])
        if not (nxt_w in dist[nxt]) or (nxt_cost < dist[nxt][nxt_w]):
            dist[nxt][nxt_w] = nxt_cost
            push(pq, (nxt_cost, nxt_w, nxt))