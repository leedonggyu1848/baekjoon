import sys
input = sys.stdin.readline
meeting = []

for _ in range(int(input())):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))
end = 0
rst = 0
for i in range(len(meeting)):
    if end <= meeting[i][0]:
        end = meeting[i][1]
        rst += 1
print(rst)