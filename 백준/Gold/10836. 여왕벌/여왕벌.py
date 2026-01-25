import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
board = [0] * (2*m-1)
for _ in range(n):
    nums = list(map(int, input().split()))
    total = sum(nums)
    cur = 2*m-1 - total + nums[0]
    i = 1
    for num in nums[1:]:
        if num > 0:
            board[cur] += i
            i = 1
        else:
            i += 1
        cur += num
        if cur >= 2*m-1:
            break
rst = [[0]*m for _ in range(m)]
cur = 1
for i,v in enumerate(board):
    cur += board[i]
    if i <= (2*m-1) // 2:
        rst[m-1-i][0] = cur
    else:
        rst[0][i-((2*m-1) // 2)] = cur
for i in range(1, m):
    for j in range(1, m):
        rst[i][j] = max(rst[i-1][j], rst[i][j-1], rst[i-1][j-1])
        
for line in rst:
    print(*line)
