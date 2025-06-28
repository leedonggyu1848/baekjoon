import sys
input = sys.stdin.readline

n = int(input())
prefix, suffix  = input().rstrip().split('*')
for _ in range(int(n)):
    s = input().rstrip()
    if len(s) < len(prefix) + len(suffix) \
        or not prefix == s[:len(prefix)] \
        or not suffix == s[len(s)-len(suffix):]:
        print("NE")
    else:
        print("DA")

