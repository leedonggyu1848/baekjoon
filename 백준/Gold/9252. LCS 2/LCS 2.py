import sys
input = sys.stdin.readline

A = input().rstrip() # y
B = input().rstrip() # x
dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]

for y, a in enumerate(A):
    for x, b in enumerate(B):
        if A[y] == B[x]:
            dp[y+1][x+1] = dp[y][x] + 1
        dp[y+1][x+1] = max(dp[y+1][x], dp[y][x+1], dp[y+1][x+1])

y = len(A)
x = len(B)
print(dp[y][x])
if dp[y][x] != 0:
    s = []
    while y and x:
        if (dp[y][x] == (dp[y-1][x-1] + 1)) and A[y-1] == B[x-1]:
            s.append(A[y-1])
            y -= 1
            x -= 1
        elif dp[y][x] == dp[y-1][x]:
            y -=1
        else:
            x -= 1

    print(''.join(reversed(s)))
