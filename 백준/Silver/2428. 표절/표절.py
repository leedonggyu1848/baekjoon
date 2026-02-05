import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
nums = list(sorted(map(lambda x:int(x) * 9, input().split())))

def upper_bound(left, right, tar):
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= tar:
            left = mid + 1
        else:
            right = mid
    return left


rst = 0
for i, num in enumerate(nums):
    tar = (num // 9) * 10
    low = upper_bound(i+1, n, tar)
    rst += low - i - 1
print(rst)
