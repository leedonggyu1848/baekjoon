import sys
input = sys.stdin.readline

s, k = map(int, input().split())
nums = list(map(int, input().split()))
start = 0
end = -1
odd = 0
even = 0

rst = 0
while end < s and start < s:
    while end < s-1:
        if nums[end + 1] % 2 and odd == k:
            break
        end += 1
        if nums[end] % 2:
            odd += 1
        else:
            even += 1
            rst = max(rst, even)
    if nums[start] % 2:
        odd -= 1
    else:
        even -= 1
    start += 1

print(rst)
