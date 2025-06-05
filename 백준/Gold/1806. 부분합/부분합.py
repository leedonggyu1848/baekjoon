import sys
import math
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

left = right = 0
rst = math.inf
cur = nums[0]

while left < n and right < n:
    if s <= cur:
        rst = min(rst, right-left+1)
    if left == right or cur < s:
        right += 1
        if right < n:
            cur += nums[right]
    else:
        cur -= nums[left]
        left += 1

print(rst if rst != math.inf else 0)
