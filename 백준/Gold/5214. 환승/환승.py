import sys
from collections import deque
input = sys.stdin.readline

def main():
    n, k, m = map(int, input().split())
    adj = [[] for _ in range(n+m)]
    for i in range(m):
        for node in list(map(lambda x:int(x)-1, input().split())):
            adj[n+i].append(node)
            adj[node].append(n+i)

    visited = [False] * (n+m)
    q = deque()
    q.append((0, 1))
    visited[0] = True
    while q:
        cur, time = q.popleft()
        if cur == n-1:
            print(time//2+1)
            return
        for nxt in adj[cur]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            q.append((nxt, time+1))
    print(-1)

main()
