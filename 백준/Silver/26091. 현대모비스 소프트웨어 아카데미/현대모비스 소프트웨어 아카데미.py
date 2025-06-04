import sys
input = sys.stdin.readline

n, m = map(int, input().split())
stat = list(map(int, input().split()))
stat.sort()

left = 0
right = len(stat) - 1
rst = 0

while left < right:
    if stat[left] + stat[right] >= m:
        left += 1
        right -= 1
        rst += 1
    else:
        left += 1

print(rst)
