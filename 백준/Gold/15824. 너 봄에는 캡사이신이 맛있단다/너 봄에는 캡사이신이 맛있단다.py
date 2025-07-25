import sys
input = sys.stdin.readline

mod = 1000000007

def double(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    v = double(n // 2)
    v = (v * v) % mod
    rst = 2 if n % 2 else 1
    rst = (rst * v) % mod
    return rst


n = int(input())
nums = list(map(int, input().split()))
nums.sort()
if n == 1:
    print(0)
else:
    rst = 0
    for i in range(n):
        rst += nums[i] * (double(i) - double(n - i - 1))
        rst %= mod
    print(rst)
