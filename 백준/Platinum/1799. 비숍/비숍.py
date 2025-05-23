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
def solve(y, x_slot, cnt):
    global rst, bits, full
    if y == n or x_slot == full:
        rst = max(rst, cnt)
        return
    if rst >= n-y+1 + cnt:
        return
    cnds = full & ~(x_slot | bits[y]) # 빈 공간 1
    while cnds:
        mask = cnds & (-cnds) # cnds 가장 오른쪽 1
        solve(y+1, x_slot ^ mask, cnt+1)
        cnds ^= mask
    solve(y+1, x_slot, cnt)

rst = 0
solve(0, 0, 0)
print(rst)
