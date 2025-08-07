import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
rst = [[0] * 2 for _ in range(n)] # (B, C)의 각 개수
init, ratio = 3, 2
I, R = 0, 1 # init, ratio 배열 위치

rst[0][I] = arr[0]
rst[1][I] = max(arr[1] - arr[0], 0)
rst[1][R] = min(arr[0], arr[1])

for i in range(2, n):
    rst[i][R] = min(min(rst[i-2][I], rst[i-1][R]) + rst[i-1][I], arr[i])
    rst[i][I] = arr[i] - rst[i][R]
answer = 0
for i in range(n):
    answer += rst[i][I] * init
    answer += rst[i][R] * ratio
print(answer)
