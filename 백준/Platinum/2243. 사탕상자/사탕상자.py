import sys
input = sys.stdin.readline

max_rank = 1000000
tree = [0] * (max_rank * 4)

def left_node(idx):
    return (idx * 2) + 1

def right_node(idx):
    return (idx * 2) + 2

def update(rank, n):
    def inner(left, right, cur):
        if not (left <= rank <= right):
            return
        tree[cur] += n
        if left == right:
            return
        mid = (left + right) // 2
        inner(left, mid, left_node(cur))
        inner(mid+1, right, right_node(cur))

    inner(1, max_rank, 0)

def search(rank):
    def inner(left, right, cur, r):
        tree[cur] -= 1
        if left == right:
            return left
        mid = (left + right) // 2
        lnode = left_node(cur)
        if tree[lnode] >= r:
            return inner(left, mid, lnode, r)
        else:
            rnode = right_node(cur)
            return inner(mid+1, right, rnode, r - tree[lnode])
    return inner(1, max_rank, 0, rank)

for _ in range(int(input())):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        print(search(lst[1]))
    else:
        update(lst[1], lst[2])

