import sys
import heapq
from collections import deque
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

# np: 발전소 개수
nv, ne, np = map(int, input().split())
powers = list(map(lambda x: int(x)-1, input().split()))
edges = []
for _ in range(ne):
    v1, v2, c = map(int, input().split())
    v1 -= 1
    v2 -= 1
    edges.append((v1, v2, c))

adj = [[-1] * nv for _ in range(nv)]
p = [-1 for _ in range(nv)]
total = 0

def union(v1, v2):
    global p
    small = find(v1)
    big = find(v2)
    if small == big:
        return False
    if p[small] > p[big]:
        small, big = big, small
    if p[small] == p[big]:
        p[small] -= 1
    p[big] = small
    return True

def find(v):
    if p[v] < 0:
        return v
    p[v] = find(p[v])
    return p[v]

def mst():
    global adj, total
    pq = []
    con_edges = []
    for edge in edges:
        v1, v2, c = edge
        push(pq, (c, v1, v2))
    while pq:
        c, v1, v2 = pop(pq)
        if union(v1, v2):
            adj[v1][v2] = c
            adj[v2][v1] = c
            total += c
            push(con_edges, (-c, v1, v2))
    return con_edges

def can_del(v1, v2):
    global adj
    c = adj[v1][v2]
    adj[v1][v2] = -1
    adj[v2][v1] = -1
    visited = [False] * nv
    for power in powers:
        visited[power] = True
        q = deque()
        q.append(power)
        while q:
            cur = q.popleft()
            for nxt, cost in enumerate(adj[cur]):
                if cost > 0 and not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
    for v in visited:
        if not v:
            adj[v1][v2] = c
            adj[v2][v1] = c
            return False
    return True

con_edges = mst()
while con_edges:
    c, v1, v2 = pop(con_edges)
    if can_del(v1, v2):
        total += c # c만큼 제거 (c는 부호변환된 상태)

print(total)
