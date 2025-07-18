from collections import deque

NOT_VISITED = 0
VISITED = 1
HOLD = 2

def solution(n, path, order):
    indgree = [0 for _ in range(n)]
    edges = [[] for _ in range(n)]
    orders = [[]for _ in range(n)]
    visited = [NOT_VISITED for _ in range(n)]
    q = deque()
    for s, e in path:
        edges[s].append(e)
        edges[e].append(s)
    for s, e in order:
        orders[s].append(e)
        indgree[e] += 1
        
    def append(tar):
        q.appendleft(tar)
        visited[tar] = VISITED
        for nxt in orders[tar]:
            indgree[nxt] -= 1
            if indgree[nxt] == 0 and visited[nxt] == HOLD:
                append(nxt)
                
    if indgree[0] == 0:
        append(0)
    while q:
        cur = q.pop()
        for nxt in edges[cur]:
            if visited[nxt] != VISITED:
                if indgree[nxt] == 0:
                    append(nxt)
                else:
                    visited[nxt] = HOLD
                        
    for cur in range(n):
        if visited[cur] != VISITED:
            return False
    return True
    