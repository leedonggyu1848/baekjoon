import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

n = int(input())
pq = []

for i in range(n):
    cost = int(input())
    push(pq, (cost, 0, i+1))

for i in range(n):
    for j, v in enumerate(map(int, input().split())):
        if i != j:
            push(pq, (v, i+1, j+1))

p = [-1] * (n+1)

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

