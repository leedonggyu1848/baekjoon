n = int(input())
people = [0] * n
for i in range(n):
    people[i] = int(input())

ret = 0
s = []

for rv in people:
    while s and s[-1][0] < rv:
        ret += 1
        s.pop()
    if s:
        if s[-1][0] == rv:
            ret += s[-1][1]
            if len(s) != s[-1][1]:
                ret += 1
        else:
            ret += 1
    cnt = 1
    if s and s[-1][0] == rv:
        cnt = s[-1][1] + 1
    s.append((rv, cnt))

print(ret)
