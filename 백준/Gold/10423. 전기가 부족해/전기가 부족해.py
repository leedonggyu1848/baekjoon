import sys
import heapq
from collections import deque
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

# np: 발전소 개수
nv, ne, np = map(int, input().split())
edges = []
powers = list(map(int, input().split()))
for _ in range(ne):
    v1, v2, c = map(int, input().split())
    edges.append((v1, v2, c))

p = [-1 for _ in range(nv+1)]
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
    for edge in edges:
        v1, v2, c = edge
        push(pq, (c, v1, v2))
    while pq:
        c, v1, v2 = pop(pq)
        if union(v1, v2):
            total += c

for power in powers:
    p[power] = 0
mst()
print(total)
