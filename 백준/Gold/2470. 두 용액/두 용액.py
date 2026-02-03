import sys
input = sys.stdin.readline

n = int(input())
nums = list(sorted(map(int, input().split())))

left, right = 0, n-1
rst = (nums[left], nums[right])
cmp = abs(nums[left] + nums[right])
while left < right:
    cur = nums[left] + nums[right]
    if cmp > abs(cur):
        rst = (nums[left], nums[right])
        cmp = abs(cur)
    if cur < 0:
        left += 1
    else:
        right -= 1
print(*rst)

