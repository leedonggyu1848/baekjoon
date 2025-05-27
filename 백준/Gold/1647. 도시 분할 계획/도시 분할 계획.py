import sys
import math
input = sys.stdin.readline

nv, ne = map(int, input().split())
edges = []

for _ in range(ne):
    s, e, c = map(int, input().split())
    if e < s:
        s, e = e, s
    edges.append((c, s, e))

def find(p, idx):
    if p[idx] < 0:
        return idx
    return find(p, p[idx])

def union(p, a, b):
    parrent = find(p, a)
    child = find(p, b)
    if parrent == child:
        return False
    if p[parrent] > p[child]:
        parrent, child = child, parrent
    elif p[parrent] == p[child]:
        p[parrent] -= 1
    p[child] = parrent
    return True

def kruscal(edges):
    global nv
    p = [-1] * (nv+1)
    rst = 0
    maxv = -1
    for c, s, e in edges:
        ps = find(p, s)
        pe = find(p, e)
        if ps == pe:
            continue
        rst += c
        maxv = max(maxv, c)
        union(p, ps, pe)
    return rst - maxv

rst = math.inf
edges.sort()
print(kruscal(edges))

