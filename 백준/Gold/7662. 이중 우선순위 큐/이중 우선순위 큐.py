import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def solve():
    def pop_one(q, mul):
        while q:
            n = mul * pop(q)
            if cnt[n] > 0:
                cnt[n] -= 1
                return n
        return None

    cnt = dict()
    minq = []
    maxq = []

    for _ in range(int(input())):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':
            push(minq, n)
            push(maxq, -n)
            cnt[n] = cnt.get(n, 0) + 1
        elif n == 1:
            pop_one(maxq, -1)
        else:
            pop_one(minq, 1)

    left = pop_one(maxq, -1)
    right = pop_one(minq, 1)

    if left == None:
        print("EMPTY")
    elif right == None:
        print(left, left)
    else:
        print(left, right)


for _ in range(int(input())):
    solve()
