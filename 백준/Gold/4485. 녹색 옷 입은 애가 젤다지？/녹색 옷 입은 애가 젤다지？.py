import sys, math
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

problem = 1
while True:
    n = int(input())
    if n == 0:
        break
    board = []
    costs = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        board.append(list(map(int, input().split())))
    pq = []
    push(pq, (board[0][0], (0, 0)))
    costs[0][0] = board[0][0]
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    while pq:
        cost, cur = pop(pq)
        if costs[cur[0]][cur[1]] != cost:
            continue
        if cur == (n-1, n-1):
            print(f"Problem {problem}: {cost}")
            break
        for i in range(4):
            y = cur[0] + dy[i]
            x = cur[1] + dx[i]
            if 0 <= y < n and 0 <= x < n:
                nxt_cost = cost + board[y][x]
                if costs[y][x] > nxt_cost:
                    costs[y][x] = nxt_cost
                    push(pq, (nxt_cost, (y, x)))

    problem += 1
