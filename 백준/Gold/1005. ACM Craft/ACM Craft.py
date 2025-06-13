import sys
from collections import deque
input = sys.stdin.readline

def solve():
    q = deque()
    for i in range(nv):
        if not ideg[i]:
            if i == tar:
                return costs[i]
            q.append((i, costs[i]))
    max_list = [0 for _ in range(nv)]
    while q:
        cur, cur_cost = q.pop()
        for nxt in adj[cur]:
            ideg[nxt] -= 1
            max_list[nxt] = max(max_list[nxt], cur_cost)
            if ideg[nxt] == 0:
                nxt_cost = max_list[nxt] + costs[nxt]
                if nxt == tar:
                    return nxt_cost
                q.append((nxt, nxt_cost))

t = int(input())
for _ in range(t):
    nv, ne = map(int, input().split())
    adj = [[] for _ in range(nv)]
    ideg = [0 for _ in range(nv)]
    costs = list(map(int, input().split()))
    for _ in range(ne):
        v1, v2 = map(lambda x:int(x)-1, input().split())
        adj[v1].append(v2)
        ideg[v2] += 1
    tar = int(input())-1
    print(solve())


