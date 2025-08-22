from collections import deque

tree = [{}, 0] # (last, {})

def get_child(tree, c):
    if c in tree[0]:
        return tree[0][c]
    tree[0][c] = [{}, -1]
    return tree[0][c]

def get_children(tree):
    return tree[0]

def get_id(tree):
    return tree[1]

def set_id(tree, id):
    tree[1] = id

def update(tree, name, id):
    if not name:
        set_id(tree, id)
        return
    update(get_child(tree, name[0]), name[1:], id)

def find(tree, name):
    q = deque()
    q.append((0, tree))
    ret = set()
    while q:
        idx, tree = q.popleft()
        if idx == len(name):
            if get_id(tree) != -1:
                ret.add(get_id(tree))
            continue
        if name[idx] == '*':
            for v in get_children(tree).values():
                q.append((idx+1, v))
        else:
            if name[idx] in get_children(tree):
                q.append((idx+1, get_child(tree, name[idx])))
    return ret

dp = [False] * (1 << 9)

def com(ban_list, bit):
    ret = 0
    if not ban_list:
        if not dp[bit]:
            ret += 1
        dp[bit] = True
        return ret
    for ban in ban_list[0]:
        if not ((1 << ban) & bit):
            ret += com(ban_list[1:], bit | (1 << ban))
    return ret
    
        
def solution(user_id, banned_id):
    for i, v in enumerate(user_id):
        update(tree, v, i)
    ban_list = [find(tree, i) for i in banned_id]
    return com(ban_list, 0)