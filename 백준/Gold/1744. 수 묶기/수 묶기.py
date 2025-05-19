import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


def pair(lst):
    rst = 0
    for i, j in zip(lst[::2], lst[1::2]):
        if i == 1 or j == 1:
            rst += i + j
        else:
            rst += i * j
    if len(lst) % 2 != 0:
        rst += lst[-1]
    return rst

arr.sort()
zero = 0
for zero, v in enumerate(arr):
    if v > 0:
        break
zero -= 1

if arr[0] > 0:
    plus = arr
    minus = []
elif arr[-1] <= 0:
    plus = []
    minus = arr
else:
    minus = arr[: zero+1]
    plus = arr[zero+1:]


print(pair(minus) + pair(list(reversed(plus))))

