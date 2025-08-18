import sys, math
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nv, ne, times = map(int, input().split())

dist = [[math.inf] * (nv+1) for _ in range(nv)]
start, end = map(int, input().split())

edges = [[] for _ in range(nv+1)]
for _ in range(ne):
    s, e, cost = map(int, input().split())
    edges[s].append((cost, e))
    edges[e].append((cost, s))

pq = []
push(pq, (0, 0, start))
dist[0][start] = 0
while pq:
    cost, cnt, cur = pop(pq)
    if dist[cnt][cur] < cost or cnt == nv-1:
        continue
    for step, nxt in edges[cur]:
        nxt_cost = cost + step
        if dist[cnt+1][nxt] <= nxt_cost:
            continue
        for i in range(cnt+1, nv):
            dist[i][nxt] = min(nxt_cost, dist[i][nxt])
        push(pq, (nxt_cost, cnt+1, nxt))

costs = [dist[cnt][end] for cnt in range(nv)]
print(min(costs))

for t in range(times):
    step = int(input())
    for i in range(nv):
        costs[i] += step * i
    print(min(costs))
