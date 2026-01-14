import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve():
    t, nv, ne = map(int, input().split())
    sr = [1] * (nv+1)
    indeg = [0] * (nv+1)
    fd = [[] for _ in range(nv+1)]
    rev = [[] for _ in range(nv+1)]
    q = deque()
    for _ in range(ne):
        a, b = map(int, input().split())
        indeg[b] += 1
        fd[a].append(b)
        rev[b].append(a)
    for i in range(1, nv+1):
        if indeg[i] == 0:
            q.append(i)
    while q:
        cur = q.popleft()
        for nxt in fd[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
                s = 0
                cnt = 0
                for bf in rev[nxt]:
                    if s == sr[bf]:
                        cnt += 1
                    elif s < sr[bf]:
                        s = sr[bf]
                        cnt = 1
                sr[nxt] = s if cnt == 1 else s + 1

    print(t, sr[nv])

for _ in range(int(input())):
    solve()
