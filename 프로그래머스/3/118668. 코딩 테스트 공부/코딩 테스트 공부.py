import math
import heapq
push = heapq.heappush
pop = heapq.heappop

lim_y = 151
lim_x = 151

def solution(alp, cop, problems):
    dp = [[99999] * lim_x for _ in range(lim_y)]
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    max_y = max((x[0] for x in problems))
    max_x = max((x[1] for x in problems))
    alp = min(alp, max_y)
    cop = min(cop, max_x)
    dp[alp][cop] = 0
            
    for y in range(alp, lim_y):
        for x in range(cop, lim_x):
            for y_req, x_req, dy, dx, cost in problems:
                if y < y_req or x < x_req:
                    continue
                ny = min(y + dy, lim_y-1)
                nx = min(x + dx, lim_x-1)
                dp[ny][nx] = min(dp[y][x] + cost, dp[ny][nx])
                    
    rst = 99999
    for y in range(max_y, lim_y):
        for x in range(max_x, lim_x):
            rst = min(rst, dp[y][x])
    return rst