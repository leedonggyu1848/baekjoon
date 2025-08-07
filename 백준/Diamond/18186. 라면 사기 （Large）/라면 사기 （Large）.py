import sys
input = sys.stdin.readline

n, init, ratio = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
if ratio >= init:
    for i in arr:
        answer += init*i
else:
    rst = [[0] * 2 for _ in range(3)] # (B, C)의 각 개수
    I, R = 0, 1 # init, ratio 배열 위치
    cache = [(arr[0], 0), (max(arr[1] - arr[0], 0), min(arr[0], arr[1]))]
    answer = (cache[0][I] + cache[1][I]) * init + (cache[0][R] + cache[1][R]) * ratio

    for i in range(2, n):
        first, second = cache
        r = min(min(first[I], second[R]) + second[I], arr[i])
        i = arr[i] - r
        answer += i * init + r * ratio
        cache = [second, (i, r)]
print(answer)

