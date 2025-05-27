import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = [(int(input()), i) for i in range(n)]
nums.sort()

class SegTree:
    def __init__(self, n):
        self.tree = [0] * (n*4)
        self.n = n
        def _inner(cur, s, e):
            if s == e:
                self.tree[cur] = 1
                return self.tree[cur]
            mid = mid_idx(s, e)
            left = _inner(lchild(cur), s, mid)
            right = _inner(rchild(cur), mid+1, e)
            self.tree[cur] = left + right
            return self.tree[cur]
        _inner(0, 0, n-1)

    def select(self, tars, tare):
        if tars > tare:
            return 0
        def _inner(cur, s, e):
            if e < tars or tare < s:
                return 0
            if tars <= s and e <= tare:
                return self.tree[cur]
            mid = mid_idx(s, e)
            left = _inner(lchild(cur), s, mid)
            right = _inner(rchild(cur), mid+1, e)
            return left + right
        return _inner(0, 0, self.n-1)

    def update(self, tar):
        def _inner(cur, s, e):
            if e < tar or tar < s:
                return
            self.tree[cur] -= 1
            if s == e:
                return
            mid = mid_idx(s, e)
            _inner(lchild(cur), s, mid)
            _inner(rchild(cur), mid+1, e)
        _inner(0, 0, self.n-1)


def lchild(pos):
    return pos * 2 + 1

def rchild(pos):
    return pos * 2 + 2

def mid_idx(s, e):
    return (s + e) // 2

tree = SegTree(n)
left = 0
right = n-1
while left < right:
    print(tree.select(0, nums[left][1]-1))
    tree.update(nums[left][1])
    print(tree.select(nums[right][1]+1, n-1))
    tree.update(nums[right][1])
    left += 1
    right -= 1
if left == right:
    print(0)

