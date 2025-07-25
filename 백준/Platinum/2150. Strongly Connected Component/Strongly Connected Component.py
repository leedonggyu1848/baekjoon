import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

nv, ne = map(int, input().split())
edges = [[] for _ in range(nv + 1)]

for _ in range(ne):
    s, e = map(int, input().split())
    edges[s].append(e)

p = [-1] * (nv + 1)
finished = [False] * (nv + 1)
idx = 0
s = []
sccs = []

def find_parent(cur):
    global idx
    idx += 1
    p[cur] = idx
    s.append(cur)

    pcur = p[cur]
    for nxt in edges[cur]:
        if p[nxt] == -1: # the first time to visit
            pcur = min(pcur, find_parent(nxt))
        elif not finished[nxt]: # visited but not finished
            pcur = min(pcur, p[nxt])
    if pcur == p[cur]: # The parent node is myself
        scc = []
        while s:
            t = s.pop()
            scc.append(t)
            finished[t] = True
            if t == cur: break
        sccs.append(tuple(sorted(scc)))
    return pcur

for i in range(1, nv):
    if not finished[i]:
        find_parent(i)

sccs.sort()
print(len(sccs))
for scc in sccs:
    print(' '.join(map(str, scc)), end = ' ')
    print('-1')
