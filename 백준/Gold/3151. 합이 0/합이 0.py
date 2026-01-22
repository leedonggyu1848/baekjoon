import sys
input = sys.stdin.readline

input()
nums = sorted(list(map(int, input().split())))

def upper_bs(lst, tar, left, right):
    while left < right:
        mid = (left + right) // 2
        if lst[mid] <= tar:
            left = mid + 1
        else:
            right = mid
    return right

def lower_bs(lst, tar, left, right):
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < tar:
            left = mid + 1
        else:
            right = mid
    return right

rst = 0
for l in range(len(nums)):
    for r in range(l+2, len(nums)):
        upper = upper_bs(nums, -(nums[l] + nums[r]), l+1, r)
        lower = lower_bs(nums, -(nums[l] + nums[r]), l+1, r)
        rst += upper - lower

print(rst)
