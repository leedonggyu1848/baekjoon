import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1 for _ in range(n)]
bf = [i for i in range(n)]
hi = 0
hi_index = 0

for i,vi in enumerate(nums):
    for j in range(0, i):
        if nums[j] < vi and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
            bf[i] = j
    if dp[i] > hi:
        hi = dp[i]
        hi_index = i

print(dp[hi_index])
i = hi_index
s = []
while True:
    s.append(nums[i])
    if bf[i] == i:
        break
    i = bf[i]
print(' '.join(map(str, reversed(s))))
