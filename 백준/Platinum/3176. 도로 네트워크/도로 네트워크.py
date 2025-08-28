import sys
import math
from collections import deque
input = sys.stdin.readline

nv = int(input())
# 1이 무조건 root
edges = [[] for _ in range(nv+1)]

for _ in range(nv-1):
    v1, v2, cost = map(int, input().split())
    edges[v1].append((v2, cost))
    edges[v2].append((v1, cost))

class Node:
    def __init__(self, n, minv=math.inf, maxv=-1):
        self.n = n
        self.minv = minv
        self.maxv = maxv

    def __repr__(self):
        return f"(n:{self.n}, minv:{self.minv}, maxv:{self.maxv})"

p = [[None] * (nv+1) for _ in range(18)]
depths = [-1] * (nv+1)
q = deque()
q.append((1, 0))
depths[1] = 0
p[0][1] = Node(1)
while q:
    cur, depth = q.popleft()
    for nxt, cost in edges[cur]:
        if depths[nxt] == -1:
            p[0][nxt] = Node(cur, cost, cost)
            depths[nxt] = depth+1
            q.append((nxt, depth+1))
max_depth = max(depths)

for i in range(1, 18):
    for n in range(1, nv+1):
        mid = p[i-1][n]
        tar = p[i-1][mid.n]
        p[i][n] = Node(tar.n, min(mid.minv, tar.minv), max(mid.maxv, tar.maxv))

def get_parent(node, i):
    nxt = p[i][node.n]
    return Node(nxt.n, min(nxt.minv, node.minv), max(nxt.maxv, node.maxv))

def find_ancestor(cur, depth):
    step = 0
    while depths[cur.n] != depth:
        nxt = get_parent(cur, step)
        if depths[nxt.n] < depth:
            break
        step += 1
        cur = nxt
    if depths[cur.n] != depth:
        return find_ancestor(cur, depth)
    return cur

def lca(v1, v2):
    step = 0
    while v1.n != v2.n:
        nxt_v1 = get_parent(v1, step)
        nxt_v2 = get_parent(v2, step)
        if nxt_v1.n == nxt_v2.n:
            if step == 0:
                return min(nxt_v1.minv, nxt_v2.minv), max(nxt_v1.maxv, nxt_v2.maxv)
            else:
                return lca(v1, v2)
        step += 1
        v1 = nxt_v1
        v2 = nxt_v2
    return min(v1.minv, v2.minv), max(v1.maxv, v2.maxv)

for _ in range(int(input())):
    deep, shallow = map(int, input().split())
    if depths[deep] < depths[shallow]:
        deep, shallow = shallow, deep
    shallow = Node(shallow)
    deep = find_ancestor(Node(deep), depths[shallow.n])
    minv, maxv = lca(shallow, deep)
    if minv == math.inf:
        minv = 0
    if maxv == -1:
        maxv = 0
    print(minv, maxv)
