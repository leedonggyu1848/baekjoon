import math

def solution(temperature, t1, t2, a, b, onboard):
    temperature += 20
    t1 += 20
    t2 += 20
    # temperature x time
    dp = [[math.inf] * 70 for _ in range(len(onboard))]
    dp[0][temperature] = 0
    for i in range(1, len(onboard)):
        for j in range(10, 61):
            if onboard[i] == 1 and not (t1 <= j <= t2):
                continue
            if j == temperature:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j+1], dp[i-1][j])
            elif j < temperature:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j+1]+a,  dp[i-1][j]+b)
            elif j > temperature:
                dp[i][j] = min(dp[i-1][j-1]+a, dp[i-1][j+1], dp[i-1][j]+b)
    rst = math.inf
    for j in range(10, 61):
        rst = min(dp[-1][j], rst)
    return rst
        