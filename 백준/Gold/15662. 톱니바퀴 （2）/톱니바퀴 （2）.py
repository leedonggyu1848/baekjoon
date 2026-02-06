import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())
chains = []
points = [(6, 2)] * t

for _ in range(t):
    chains.append(input().rstrip())

def align(pos):
    return ((pos[0] + 8) % 8, (pos[1] + 8) % 8)

def rotate(chain, d):
    point = points[chain]
    points[chain] = align((point[0] - d, point[1] - d))

def can_right(chain):
    if chain == t-1:
        return False
    return chains[chain][points[chain][1]] != chains[chain+1][points[chain+1][0]]

def can_left(chain):
    if chain == 0:
        return False
    return chains[chain][points[chain][0]] != chains[chain-1][points[chain-1][1]]

for _ in range(int(input())):
    chain, d = map(int, input().split())
    chain -= 1
    jobs = [(chain, d)]
    curd = d
    cur_chain = chain
    while(can_right(cur_chain)):
        cur_chain += 1
        curd *= -1
        jobs.append((cur_chain, curd))
    curd = d
    cur_chain = chain
    while(can_left(cur_chain)):
        cur_chain -= 1
        curd *= -1
        jobs.append((cur_chain, curd))
    for chain, d in jobs:
        rotate(chain, d)


rst = 0
for i, point in enumerate(points):
    tmp = (point[0]+2, point[1]-2)
    tmp = align(tmp)
    if chains[i][tmp[0]] == '1':
        rst += 1
print(rst)

