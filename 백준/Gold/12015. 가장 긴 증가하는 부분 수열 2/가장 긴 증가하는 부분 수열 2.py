import sys
import bisect
input = sys.stdin.readline

int(input())
dp = []
for n in map(int, input().split()):
    i = bisect.bisect_left(dp, n)
    if i == len(dp):
        dp.append(n)
    else:
        dp[i] = n
print(len(dp))
