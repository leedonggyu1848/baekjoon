import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
nums = list(sorted(map(int, input().split())))

def judge(base):
    rst = 0
    for num in nums:
        rst += max((num - base), 0)
    return rst >= m

def solve():
    left = 0
    right = nums[-1]
    ret = 0
    while left <= right:
        mid = (left + right) // 2
        if judge(mid):
            ret = mid
            left = mid + 1
        else:
            right = mid - 1
    return ret

print(solve())

