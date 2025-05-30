import sys
input = sys.stdin.readline

def left_child(idx):
    return idx * 2 + 1

def right_child(idx):
    return idx * 2 + 2

class SegTree:
    def __init__(self, emts):
        def _inner(left, right, node):
            if left == right:
                self.tree[node] = emts[left]
                return self.tree[node]
            mid = (left + right) // 2
            left_v = _inner(left, mid, left_child(node))
            right_v = _inner(mid+1, right, right_child(node))
            self.tree[node] = left_v + right_v
            return self.tree[node]

        self.root = 0
        self.n = len(emts)
        self.tree = [0] * (self.n*4) # 보통 4배로 설정
        # 가장 큰 인덱스 범위(트리 인덱스는 아님), 첫번째 트리 인덱스
        _inner(0, self.n-1, self.root)

    def search(self, lo, hi):
        def _inner(left, right, node):
            # 탐색하는 범위 벗어남 (0은 항등원)
            if hi < left or right < lo:
                return 0
            # 탐색 범위 안에 들어옴
            if lo <= left and right <= hi:
                return self.tree[node]
            mid = (left + right) // 2
            return _inner(left, mid, left_child(node)) + _inner(mid+1, right, right_child(node))

        # 가장 큰 인덱스 범위(트리 인덱스는 아님), 첫번째 트리 인덱스
        return _inner(0, self.n-1, self.root)

    def update(self, tar, v):
        def _inner(left, right, node):
            if tar < left or right < tar:
                return
            self.tree[node] += v
            if left == right:
                return
            mid = (left + right) // 2
            _inner(left, mid, left_child(node))
            _inner(mid+1, right, right_child(node))

        _inner(0, self.n-1, self.root)

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
tree = SegTree(nums)
for _ in range(m + k):
    t, a, b = map(int, input().split())
    if t == 1:
        tree.update(a-1, b - nums[a-1])
        nums[a-1] = b
    elif t == 2:
        print(tree.search(a-1, b-1))
