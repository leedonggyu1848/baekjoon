import sys
input = sys.stdin.readline

_n = int(input())
n = 2*_n - 1
board = [[False] * n for _ in range(n)]
for y in range(n):
    x = (n // 2) - y
    for e in map(int, input().split()):
        if e == 1:
            board[y][x] = True
        y += 1
        x += 1

bits = [0 for i in range(n)] # 사용하면 1
for y in range(n):
    for x in range(n):
        if not board[y][x]:
            bits[y] |= 1 << x

full = (1 << n) - 1
dp = [[-1] * (full+1) for _ in range(n)]
def solve(y, x_slot, cnt):
    global bits, full
    if y == n or x_slot == full:
        return 0
    if dp[y][x_slot] != -1:
        return dp[y][x_slot]
    cnds = full & ~(x_slot | bits[y]) # 빈 공간 1
    while cnds:
        mask = cnds & (-cnds) # cnds 가장 오른쪽 1
        dp[y][x_slot] = max(dp[y][x_slot], solve(y+1, x_slot ^ mask, cnt+1)+1)
        cnds ^= mask
    dp[y][x_slot] = max(dp[y][x_slot], solve(y+1, x_slot, cnt))
    return dp[y][x_slot]

print(solve(0, 0, 0))
