import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nv, ne = map(int, input().split())
# 오르막 True, 내리막 False
edges = []
for _ in range(ne + 1):
    v1, v2, asc = map(int, input().split())
    asc = False if asc else True
    edges.append((v1, v2, asc))

def union(p, v1, v2):
    small = find(p, v1)
    big = find(p, v2)
    if small == big:
        return False
    if p[small] > p[big]:
        small, big = big, small
    if p[small] == p[big]:
        p[small] -= 1
    p[big] = small
    return True

def find(p, v):
    if p[v] < 0:
        return v
    p[v] = find(p, p[v])
    return p[v]

def mst(asc):
    # asc가 True면 asc를 cost 0으로 계산
    def cost(v):
        if asc:
            return 0 if v else 1
        else:
            return 1 if v else 0
    p = [-1 for _ in range(nv+1)]
    pq = []
    rst = 0
    for edge in edges:
        v1, v2, t = edge
        c = cost(t)
        push(pq, (c, v1, v2))
    while pq:
        c, v1, v2 = pop(pq)
        if union(p, v1, v2):
            if c == 0:
                rst += 1
    return rst

asc_cnt = mst(True)
desc_cnt = mst(False)
print(asc_cnt**2 - (nv - desc_cnt)**2)
