import sys
input = sys.stdin.readline

n = int(input())
cnd = (1 << n) - 1
rst = 0

# %s: % of y
def n_queen(x, ys, pdgs, ndgs):
    global n, rst, cnd
    if x == n:
        rst += 1
# ys, pdgs, ndgs에서 사용한 위치의 합집합
# cnd(후보자)에서 제거
    y_cnd = cnd & ~(ys | pdgs | ndgs)
    while y_cnd:
        mask = -y_cnd
# 오른쪽 끝 후보자 추출
        y = y_cnd & mask
        n_queen(x+1, ys|y, (pdgs|y) << 1, (ndgs|y) >> 1)
        y_cnd ^= y

# 대칭성을 이용
# => y의 반만 계산하면 됨
half = n >> 1
for y in range(half):
    ys = 1 << y
# 양의 대각선(증가함수)는 x, y에 있다면 x+1에서는 y+1을 차지당함
# 음의 대각선(감소함수)는 x, y에 있다면 x+1에서는 y-1을 차지당함
    n_queen(1, ys, ys << 1, ys >> 1)
rst *= 2

# 홀수면 y==half인 경우 계산하여 추가
# => 가운데는 대칭이 없기 때문에 따로 계산
if n % 2:
    ys = 1 << half
    n_queen(1, ys, ys << 1, ys >> 1)
print(rst)
