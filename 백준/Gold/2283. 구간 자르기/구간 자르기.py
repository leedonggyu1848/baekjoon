import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    cnt_diff = {}
    for _ in range(n):
        s, e = map(int, input().split())
        cnt_diff[s] = cnt_diff.get(s, 0) + 1
        cnt_diff[e] = cnt_diff.get(e, 0) - 1

    left = 0
    right = 0
    left_cnt = 0
    right_cnt = 0
    length = 0
    left_change = True
    right_change = True
    if length == k:
        print(left, right)
        return
    while left <= 1000000 and right <= 1000000 :
        if right_change:
            right_cnt += cnt_diff.get(right, 0)
            right_change = False
        if left_change:
            left_cnt += cnt_diff.get(left, 0)
            left_change = False
        if length < k:
            right += 1
            length += right_cnt
            right_change = True
        else:
            left += 1
            length -= left_cnt
            left_change = True
        if length == k:
            print(left, right)
            return
    print('0 0')
solve()
