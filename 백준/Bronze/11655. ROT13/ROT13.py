import sys
input = sys.stdin.readline

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
rst = []
for c in input().rstrip():
    if c in upper:
        rst.append(upper[(ord(c) - ord('A') + 13) % len(upper)])
    elif c in lower:
        rst.append(lower[(ord(c) - ord('a') + 13) % len(lower)])
    else:
        rst.append(c)
print("".join(rst))
