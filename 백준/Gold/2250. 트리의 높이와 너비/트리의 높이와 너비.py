import sys
from collections import deque
input = sys.stdin.readline

nv = int(input())
is_child = [False] * (nv + 1)
class Node:
    def __init__(self, num):
        self.num = num
tree = [Node(i) for i in range(nv + 1)]
for _ in range(nv):
    node, left, right = map(int, input().split())
    tree[node].left = left
    tree[node].right = right
    is_child[left] = True
    is_child[right] = True

for root in range(1, nv+1):
    if not is_child[root]:
        break;

x = 1
x_pos = [-1] * (nv+1)
def visit(node):
    global x
    if tree[node].left != -1:
        visit(tree[node].left)
    x_pos[node] = x
    x += 1
    if tree[node].right != -1:
        visit(tree[node].right)
visit(root)

q = deque()
q.append((root, 1))
most_left = [float('inf')] * (nv+1)
most_right = [-1] * (nv+1)

while q:
    cur, depth = q.popleft()
    most_left[depth] = min(most_left[depth], x_pos[cur])
    most_right[depth] = max(most_right[depth], x_pos[cur])
    if tree[cur].left != -1:
        q.append((tree[cur].left, depth +1))
    if tree[cur].right != -1:
        q.append((tree[cur].right, depth +1))
v = -1
level = 0
for i in range(nv+1):
    if most_left[i] != float('inf') and most_right[i] != -1:
        if most_right[i] - most_left[i] + 1 > v:
            v = most_right[i] - most_left[i] + 1
            level = i
print(level, v)
