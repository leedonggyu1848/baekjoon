import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def main():
    n = int(input())
    tree = [[] for _ in range(n)]
    dp = [[-1, -1] for _ in range(n)]
    visited = [False] * n

    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)

    def search(i):
        nonlocal visited, dp

        dp[i] = [0, 1]
        for nxt in tree[i]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            search(nxt)
            dp[i][0] += dp[nxt][1]
            dp[i][1] += min(dp[nxt])
        return min(dp[i])

    visited[0] = True
    print(search(0))

main()
