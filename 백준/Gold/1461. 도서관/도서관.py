import sys
input = sys.stdin.readline

n, capa = map(int, input().split())
left = []
right = []
for v in list(map(int, input().split())):
    if v < 0:
        left.append(-v)
    else:
        right.append(v)
left.sort()
right.sort()

def cal_first(lst):
    if not lst:
        return 0
    i = len(lst)-1
    ret = 0
    while i >= 0:
        ret += lst[i]
        for _ in range(capa):
            i -= 1
    return ret * 2

def cal_later(lst):
    if not lst:
        return 0
    i = len(lst) - 1
    ret = lst[i]
    for _ in range(capa):
        i -= 1
    while i >= 0:
        ret += lst[i] * 2
        for _ in range(capa):
            i -= 1
    return ret

left_first = cal_first(left)
left_later = cal_later(left)
right_first = cal_first(right)
right_later = cal_later(right)

print(min(left_first + right_later, left_later + right_first))

