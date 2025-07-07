class trie:
    def __init__(self):
        self.cnt = 0
        self.nxt = [None] * 26

def update(root, s):
    cur = root
    for c in s:
        idx = ord(c) - ord('a')
        if cur.nxt[idx] == None:
            cur.nxt[idx] = trie()
        cur = cur.nxt[idx]
        cur.cnt += 1

def find(root, s):
    cur = root
    ret = 0
    for c in s:
        idx = ord(c) - ord('a')
        cur = cur.nxt[idx]
        ret += 1
        if cur.cnt == 1:
            return ret
    return ret


def solution(words):
    root = trie()
    for word in words:
        update(root, word)
    ret = 0
    for word in words:
        ret += find(root, word)
    return ret