import math
# Y each 30s, 10
# M each 60s, 15

def cal_cost(time, cost):
    global data
    ret = 0
    for i in data:
        ret += math.ceil((i+time) // time) * cost
    return ret

n = int(input())
data = list(map(int, input().split()))
y = cal_cost(30, 10)
m = cal_cost(60, 15)

if y > m:
    print("M", m)
elif y < m:
    print("Y", y)
else:
    print("Y M", y)
