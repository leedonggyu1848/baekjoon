import sys
import math
input = sys.stdin.readline

n = int(input())
w = int(input())
spots = [(1,1), (n, n)]
for _ in range(w):
    y, x = map(int, input().split())
    spots.append((y, x))

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 한 차(사건으로 간 차)는 spots[a]에 있고 다른 차는 spots[b]에 있음
# 이 때 움직인 거리
dp = [[math.inf] * len(spots) for _ in range(len(spots))]
bf = [[-1] * len(spots) for _ in range(len(spots))]
moving = [[None] * len(spots) for _ in range(len(spots))]

dp[1][0] = 0 # 한 차가 spots[1]에 있고 다른 차는 spots[0]에 있음
dp[0][1] = 0 # 한 차가 spots[0]에 있고 다른 차는 spots[1]에 있음
dp[2][0] = dist(spots[1], spots[2]) # spots[1]에 있는 차가 움직임 spots[0]은 가만히 있음
moving[2][0] = False # 2번차가 움직임
dp[2][1] = dist(spots[0], spots[2]) # spots[0]에 있는 차가 움직임
moving[2][1] = True  # 1번차가 움직임


for cur in range(3, len(spots)):
    prev = cur-1
    for other in range(prev):
        # 움직였던 차가 또 움직임
        moving_prev =  dp[prev][other] + dist(spots[prev], spots[cur])
        if moving_prev < dp[cur][other]:
            dp[cur][other] = moving_prev
            bf[cur][other] = other
            moving[cur][other] = moving[prev][other]
        # 안움직인 차가 움직임
        moving_other = dp[prev][other] + dist(spots[other], spots[cur])
        if moving_other < dp[cur][prev]:
            dp[cur][prev] = moving_other
            bf[cur][prev] = other
            moving[cur][prev] = not moving[prev][other]

answer = math.inf
end = -1
for i in range(len(spots)):
    if answer > dp[-1][i]:
        answer = dp[-1][i]
        end = i
i = end
j = len(spots) - 1
s = []
while j > 1:
    s.append(1 if moving[j][i] else 2)
    i = bf[j][i]
    j -= 1

print(answer)
print(*s[::-1], sep='\n')
