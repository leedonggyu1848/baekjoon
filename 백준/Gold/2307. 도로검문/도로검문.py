import sys
import math
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nv, ne = map(int, input().split())
edges = [[] for _ in range(nv+1)]
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    edges[v1].append((v2, cost))
    edges[v2].append((v1, cost))

prev = [-1] * (nv + 1)
def dijkstra(s1, s2):
    dist = [math.inf] * (nv + 1)
    dist[1] = 0
    q = []
    push(q, (0, 1))
    while q:
        cur_cost, cur_node = pop(q)
        if cur_cost > dist[cur_node]:
            continue
        for nxt_node, step in edges[cur_node]:
            nxt_cost = cur_cost + step
            if nxt_cost < dist[nxt_node] and (cur_node, nxt_node) != (s1, s2) and (cur_node, nxt_node) != (s2, s1):
                dist[nxt_node] = nxt_cost
                prev[nxt_node] = cur_node
                push(q, (nxt_cost, nxt_node))
    return dist

normal_time = dijkstra(1, nv)[nv]
targets = []
cur = nv
while prev[cur] != -1 and cur != 1:
    targets.append((cur, prev[cur]))
    cur = prev[cur]

delay_time = normal_time
for v1, v2 in targets:
    delay_time = max(dijkstra(v1, v2)[nv], delay_time)
rst = delay_time - normal_time
print(rst if rst != math.inf else -1)

