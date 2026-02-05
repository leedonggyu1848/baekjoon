import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
push = heapq.heappush
pop = heapq.heappop

nv, ne = map(int, input().split())
pq = []
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    push(pq, (cost, v1, v2))

p = [-1] * (nv+1)
def find(v):
    if p[v] < 0:
        return v
    p[v] = find(p[v])
    return p[v]
def union(v1, v2):
    pv1 = find(v1)
    pv2 = find(v2)
    if pv1 == pv2:
        return False
    p[pv1] = pv2
    return True

rst = 0
while pq:
    cost, v1, v2 = pop(pq)
    if union(v1, v2):
        rst += cost
print(rst)
