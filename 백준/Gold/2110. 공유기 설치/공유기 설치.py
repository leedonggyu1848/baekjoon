import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
left = 0
right = arr[-1] - arr[0]

def cal_cnt(dist):
    ret = 1
    prev = 0 # 공유기 위치
    nxt = 1 # 다음 공유기 위치
    while prev < n and nxt < n:
        nxt = prev + 1
        while nxt < n and arr[nxt] - arr[prev] < dist:
            nxt += 1
        prev = nxt
        if nxt != n:
            ret += 1
    return ret


rst = -1
while left <= right:
    mid = (left + right) // 2
    cnt = cal_cnt(mid)
    if cnt < c:
        right = mid - 1
    else:
        rst = max(rst, mid)
        left = mid + 1


print(rst)
