import sys
import math
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    n1, n2 = map(int, input().split())
    arr.append((n1, n2))

dp = [[-1] * n for _ in range(n)]

def find(s, e):
    if dp[s][e] != -1:
        return dp[s][e]
    if s == e:
        dp[s][e] = 0
        return dp[s][e]
    if e - s == 1:
        dp[s][e] = arr[s][0] * arr[s][1] * arr[e][1]
        return dp[s][e]
    rst = math.inf
    cache = arr[s][0]*arr[e][1]
    for k in range(s, e):
        rst = min(rst, find(s, k)+find(k+1, e)+cache*arr[k][1])
    dp[s][e] = rst
    return dp[s][e]

print(find(0, n-1))
