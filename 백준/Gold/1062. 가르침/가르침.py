import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
bits = []
alpha = { chr(ord('a') + i):i for i in range(26) }
for _ in range(n):
    bit = 0
    for c in input().strip():
        bit |= 1 << alpha[c]
    bits.append(bit)

rst = 0
for mask in range(1 << 26):
    if mask.bit_count() != k:
        continue
    cnt = 0
    for bit in bits:
        if (bit | mask) == mask:
            cnt += 1
    rst = max(rst, cnt)

print(rst)
