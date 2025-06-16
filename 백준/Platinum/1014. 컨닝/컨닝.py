import sys
input = sys.stdin.readline

def solve():
    sy, sx = map(int, input().split())
    board = [0] * sx
    dp = [[-1] * (1 << sy) for _ in range(sx)] # x X 이전 열 위치들
    for y in range(sy):
        s = input()
        for x in range(sx):
            if s[x] =='x':
                board[x] |= 1 << y

    def mask(prev, x):
        mask = board[x] | prev | (prev >> 1) | (prev << 1)
        return mask

    def dfs(x, prev):
        nonlocal dp
        if x == sx:
            return 0
        if dp[x][prev] != -1:
            return dp[x][prev]
        dp[x][prev] = 0
        m = mask(prev, x)
        for cur in range(1 << sy):
            if not (cur & m):
                dp[x][prev] = max(dfs(x+1, cur) + cur.bit_count(), dp[x][prev])
        return dp[x][prev]

    m = mask(0, 0)
    for cur in range(1 << sy):
        if not (cur & m):
            dp[0][0] = max(dfs(1, cur) + cur.bit_count(), dp[0][0])

    print(dp[0][0])

t = int(input())
while t:
    solve()
    t -= 1
