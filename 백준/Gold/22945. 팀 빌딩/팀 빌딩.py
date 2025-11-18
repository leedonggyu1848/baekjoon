import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
left = 0
right = n-1

rst = 0

def cal_value(left, right):
    return (right - left - 1) * min(nums[left], nums[right])

while left < right:
    rst = max(rst, cal_value(left, right))
    if nums[left] < nums[right]:
        left = left + 1
    else:
        right = right - 1
print(rst)
