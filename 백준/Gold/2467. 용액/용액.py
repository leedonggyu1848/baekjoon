import sys
import math
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

minv = math.inf
lrst, rrst = 0, 0
left, right = 0, len(nums)-1
while left < right:
    v = nums[left] + nums[right]
    if minv > abs(v):
        minv = abs(v)
        lrst = nums[left]
        rrst = nums[right]
    if v < 0:
        left += 1
    else:
        right -= 1

if lrst > rrst:
    lrst, rrst = rrst, lrst
print(lrst, rrst)
