import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    maxv = -1
    rst = 0
    for p in arr[::-1]:
        if maxv < p:
            maxv = p
        else:
            rst += (maxv - p)
    print(rst)

t = int(input())
for _ in range(t):
    solve()
