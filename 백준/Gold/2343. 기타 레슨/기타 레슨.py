import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

def count_splited(length):
    cnt = 1
    cur = 0
    if length < nums[-1]:
        return math.inf
    for num in nums[::-1]:
        if cur + num <= length:
            cur += num
        else:
            cnt += 1
            cur = num
    return cnt


def find_bin(left, right):
    rst = math.inf
    while left <= right:
        mid = (left + right) // 2
        if count_splited(mid) <= m:
            rst = min(mid, rst)
            right = mid-1
        else:
            left = mid+1
    return rst

print(find_bin(max(nums), sum(nums)))


