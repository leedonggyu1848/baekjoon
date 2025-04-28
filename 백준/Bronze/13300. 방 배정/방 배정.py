n, lim = map(int, input().split())
students = [[0 for _ in range(2)] for _ in range(6)] # 6 x 2

for _ in range(n):
    sex, year = map(int, input().split())
    students[year-1][sex] += 1
ret = 0
for i in range(6):
    for j in range(2):
        ret += (students[i][j] + lim - 1) // lim
print(ret)
