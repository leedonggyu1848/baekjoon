import sys

nums = [0]

class Solve():
    def __init__(self, n, nums):
        self.n = n
        self.nums = nums
        self.sgm = [0 for _ in range(n*4)]
        def inner(node, start, end):
            if start == end:
                self.sgm[node] = self.nums[start]
                return self.sgm[node]
            mid = (start+end) // 2
            self.sgm[node] = inner(node*2, start, mid) + inner(node*2+1, mid+1, end)
            return self.sgm[node]
        inner(1, 1, self.n)

    def sum(self, left, right):
        def inner(start, end, node):
            if left > end or right < start: return 0
            if left <= start and right >= end: return self.sgm[node]
            mid = (start+end) // 2
            return inner(start, mid, node*2) + inner(mid+1, end, node*2+1)

        return inner(1, self.n, 1)

    def update(self, index, diff):
        def inner(start, end, node):
            if index < start or index > end: return
            self.sgm[node] += diff
            if start == end: return
            mid = (start+end) // 2
            inner(start, mid, node*2)
            inner(mid+1, end, node*2+1)
        inner(1, self.n, 1)


n, m, k = map(int, sys.stdin.readline().split(' '))
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
solve = Solve(n, nums)
for _ in range(m + k):
    case, bf, af = map(int, sys.stdin.readline().split(' '))
    if case == 1:
        solve.update(bf, af - nums[bf])
        nums[bf] = af
    elif case == 2:
        print(solve.sum(bf, af))