import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nv, ne, start, end, budget = map(int, input().split())
edges = [list() for _ in range(nv+1)]
costs = set()
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    edges[v1].append((cost, v2))
    edges[v2].append((cost, v1))
    costs.add(cost)
costs = sorted(list(costs))

def dijkstra(start, limit):
    global nv, edges
    dist = [math.inf] * (nv+1)
    q = []
    push(q, (0, start))
    dist[start] = 0
    while q:
        cur_cost, cur = pop(q)
        if cur_cost != dist[cur]:
            continue
        for edge in edges[cur]:
            cost, nxt = edge
            if cost > limit:
                continue
            if dist[nxt] > cost + dist[cur]:
                dist[nxt] = cost+dist[cur]
                push(q, (dist[nxt], nxt))
    return dist

rst = math.inf
def bsearch(left, right, start, end):
    global rst, costs, budget
    if left > right:
        return
    mid = (left + right) // 2
    cost = dijkstra(start, costs[mid])[end]
    if cost > budget:
        bsearch(mid+1, right, start, end)
    else:
        rst = min(rst, costs[mid])
        bsearch(left, mid-1, start, end)

bsearch(0, len(costs)-1, start, end)
print(rst if rst != math.inf else -1)

