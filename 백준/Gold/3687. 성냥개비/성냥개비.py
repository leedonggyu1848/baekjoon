import sys
input = sys.stdin.readline

arr = [(2, '1'), (3, '7'), (4, '4'), (5, '2'), (6, '0'), (7, '8')]
dp = [None for _ in range(101)]
for cnt, v in arr:
    dp[cnt] = v
dp[6] = '6'
maximum = '9' * 100

def gt(s1, s2):
    if len(s1) > len(s2):
        return True
    elif len(s1) < len(s2):
        return False
    return s1 > s2

def min_v(n):
    global dp

    if n < 2:
        return maximum
    if dp[n] != None:
        return dp[n]
    rst = maximum
    for cnt, v in arr:
        cur = min_v(n - cnt) + v
        if gt(rst, cur):
            rst = cur
    dp[n] = rst
    return dp[n]

def max_v(n):
    rst = ''
    if n % 2 == 1:
        rst = '7'
        n -= 3
    return rst + '1'*(n//2)

for _ in range(int(input())):
    n = int(input())
    print(min_v(n), max_v(n))
