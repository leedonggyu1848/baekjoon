import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

n = int(input())
edges = []


for i in range(n):
    for j, cost in enumerate(map(int, input().split())):
        if i < j:
            push(edges, (cost, i, j))

p = [-1] * n

def find(v1):
    if p[v1] < 0:
        return v1
    p[v1] = find(p[v1])
    return p[v1]

def union(v1, v2):
    pv1 = find(v1)
    pv2 = find(v2)
    if pv1 == pv2:
        return False
    p[pv2] = pv1
    return True

rst = 0
while edges:
    cost, v1, v2 = pop(edges)
    if union(v1, v2):
        rst += cost
print(rst)