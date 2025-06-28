import sys
from collections import defaultdict
input = sys.stdin.readline

player = defaultdict(int)
for _ in range(int(input())):
    player[input()[0]] += 1
rst = [c for c in sorted(player.keys()) if player[c] >= 5]
if rst:
    print("".join(rst))
else:
    print("PREDAJA")