import sys
input = sys.stdin.readline

t = int(input())
input()
a = list(map(int, input().split()))
input()
b = list(map(int, input().split()))

def acc_sum(lst):
    rst = []
    for i in range(len(lst)):
        cur_sum = 0
        for j in range(i, len(lst)):
            cur_sum += lst[j]
            rst.append(cur_sum)
    return rst

def add_cnt(acc):
    rst = []
    cur = acc[0]
    cur_cnt = 0
    for i in acc:
        if cur != i:
            rst.append((cur, cur_cnt))
            cur_cnt = 0
            cur = i
        cur_cnt += 1
    rst.append((cur, cur_cnt))
    return rst

a_sum = add_cnt(sorted(acc_sum(a)))
b_sum = add_cnt(sorted(acc_sum(b)))

left, right = 0, len(b_sum)-1
rst = 0
while left < len(a_sum) and right >= 0:
    if a_sum[left][0] + b_sum[right][0] == t:
        rst += a_sum[left][1] * b_sum[right][1]
    if a_sum[left][0] + b_sum[right][0] < t:
        left += 1
    else:
        right -= 1
print(rst)
