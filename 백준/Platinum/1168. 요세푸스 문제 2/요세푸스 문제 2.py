import sys
input = sys.stdin.readline

def left_child(idx):
    return idx * 2 + 1

def right_child(idx):
    return idx * 2 + 2

class SegTree:
    def __init__(self, n):
        def _inner(left, right, node):
            if left == right:
                self.tree[node] = 1
                return self.tree[node]
            mid = (left + right) // 2
            self.tree[node] = _inner(left, mid,left_child(node)) + _inner(mid+1,right,right_child(node))
            return self.tree[node]

        self.n = n
        self.tree = [0] * self.n * 4
        self.root = 0
        _inner(0, self.n-1, self.root)

    def update(self, k):
        def _inner(left, right, node, k):
            self.tree[node] -= 1
            if left == right:
                return left
            mid = (left + right) // 2
            left_node = left_child(node)
            right_node = right_child(node)
            if k < self.tree[left_node]:
                return _inner(left, mid, left_node, k)
            else:
                return _inner(mid+1, right, right_node, k-self.tree[left_node])
        return _inner(0, self.n-1, self.root, k)

n, k = map(int, input().split())
tree = SegTree(n)
cur = k - 1
cur_n = n
rst = []
for _ in range(n):
    rst.append(tree.update(cur)+1)
    cur_n -= 1
    if cur_n != 0:
        cur = (cur + k - 1) % cur_n

print('<', ', '.join(map(str,rst)), '>', sep='')
