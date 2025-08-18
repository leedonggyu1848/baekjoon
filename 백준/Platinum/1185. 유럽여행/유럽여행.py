import sys, math
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop


nv, ne = map(int, input().split())
toll = [math.inf]
for _ in range(nv):
    toll.append(int(input()))
pq = []
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    push(pq, (cost*2 + toll[v1] + toll[v2], v1, v2))

def uni(p, v1, v2):
    pv1 = find(p, v1)
    pv2 = find(p, v2)
    if pv1 == pv2:
        return False
    p[pv1] = pv2
    return True

def find(p, v):
    if p[v] == -1:
        return v
    p[v] = find(p, p[v])
    return p[v]

p = [-1] * (nv+1)
ret = 0
while pq:
    cost, v1, v2 = pop(pq)
    if not uni(p, v1, v2):
        continue
    ret += cost
print(ret + min(toll))
