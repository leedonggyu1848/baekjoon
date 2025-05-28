import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dp = [[[-1] * 5 for _ in range(5)] for _ in range(100001)]
MID, UP, LEFT, DOWN, RIGHT  = 0, 1, 2, 3, 4

def cal_cost(src, dest):
    if src == dest:
        return 1
    if src == MID:
        return 2
    if abs(src - dest) == 2:
        return 4
    return 3

def solve(left, right, step, seq):
    if left == right and step != 0:
        return math.inf
    if step == len(seq):
        return 0
    if dp[step][left][right] != -1:
        return dp[step][left][right]
    tar = seq[step]
    left_feet =  solve(tar, right, step+1, seq) + cal_cost(left, tar)
    right_feet = solve(left, tar, step+1, seq) + cal_cost(right, tar)
    dp[step][left][right] = min(left_feet, right_feet)
    return dp[step][left][right]

seq = list(map(int, input().split()))
print(solve(MID, MID, 0, seq[:-1]))
