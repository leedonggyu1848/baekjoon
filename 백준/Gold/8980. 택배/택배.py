import sys
input = sys.stdin.readline

# brute force
# 각 마을 사이에 박스가 얼마나 로드가 되어있는지 표기하는 것
# O(MN^2) => 20억 => x

# greedy O(CMlogM) => 정렬 알고리즘
# 이 문제가 optimal substructure 즉, local optimal이 global optimal의 일부가 되는가?
# 시작지점을 start, 도착지점을 end라 할 때
# end지점 까지의 optimal을 구할 수 있으면 그것이 global optimal의 일부가 됨
# 왜냐하면 end지점까지 짐을 옮겼다면 start지점이 어디든 같기 때문
# => 즉, end값을 기준으로 생각한다면, 어떤 end점에서의 local한 optimal값을 찾을 수 있음

# greedy choice property 즉, 현재 local optimal이 다른 local optimal들에 영향을 미치지 않는가
# => 최대 용량이 있어 평범한 방법으로는 과거 지점에서 실은 짐이 미래 지점까지 영향을 준다.
# (회의실 문제처럼 시작, 끝점만 비교하는 것으론 풀기 어려움)
# 이 문제를 여러개의 회의실이 있는 문제로 나누어 생각하면 미래에 영향을 주지 않을 수 있다.

n, c = map(int, input().split())
pk = []
waiting = [[] for _ in range(n+1)]
rst = 0

for _ in range(int(input())):
    s, e, v = map(int, input().split())
    pk.append((s, e, v))

pk.sort(key=lambda x:x[1])
slots = [None] * c

for s, e, v in pk:
    for i in range(len(slots)):
        if not slots[i] or slots[i][1] <= s:
            slots[i] = (s, e)
            rst += 1
            v -= 1
        if v == 0:
            break

print(rst)
