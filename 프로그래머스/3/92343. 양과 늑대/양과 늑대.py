from collections import deque
S = 0
W = 1

def is_sheep(node):
    return node[1] == S

def get_children(node):
    return node[2:]

def cnt_sheep(q, tree, sheep, wolf):
    loop = len(q)
    rst = sheep
    for _ in range(loop):
        cur = q.pop()
        if is_sheep(cur):
            new_sheep = sheep + 1
            new_wolf = wolf
        else:
            new_sheep = sheep
            new_wolf = wolf + 1
        children = get_children(cur)
        if new_sheep <= new_wolf:
            q.appendleft(cur)
            continue
        for child in children:
            q.appendleft(tree[child])
        rst = max(rst, cnt_sheep(q, tree, new_sheep, new_wolf))
        for _ in children:
            q.popleft()
        q.appendleft(cur)
    return rst
        
    
def solution(info, edges):
    tree = [[i, j] for i,j in enumerate(info)] # [0]: 0: 양, 1: 늑대 | [1], [2]: 자식노드
    for p, c in edges:
        tree[p].append(c)
    q = deque()
    q.append(tree[0])
    return cnt_sheep(q, tree, 0, 0)
    
    
