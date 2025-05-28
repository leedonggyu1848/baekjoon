import sys
from itertools import combinations
input = sys.stdin.readline

n_stock, lim_cost = map(int, input().split())
stocks = list(map(int, input().split()))
mid = n_stock >> 1
left = []
right = []

for i in range(mid+1):
    tmp = [e for e in map(sum, combinations(stocks[:mid], i)) if e <= lim_cost]
    left.extend(tmp)

for i in range(n_stock-mid+1):
    tmp = [e for e in map(sum, combinations(stocks[mid:], i)) if e <= lim_cost]
    right.extend(tmp)

def le(lst, tar):
    left, right = 0, len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] <= tar:
            left = mid + 1
        else:
            right = mid - 1
    return left

right.sort()
rst = 0
for i in left:
    idx = le(right, lim_cost - i)
    if idx == 0:
        rst += right[idx] <= lim_cost - i
    else:
        rst += idx + (right[idx] <= lim_cost - i)

print(rst)
