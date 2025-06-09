import math

class Node:
    def __init__(self, n):
        self.childs = []
        self.parrent = None
        self.cnt = 0
        self.num = n
        
    def add_child(self, child):
        self.childs.append(child)
        child.parrent = self
    
    def cal_cnt(self):
        if self.cnt != 0:
        	return self.cnt
       	self.childs.sort(key=lambda x:x.num)
       	ret = 0
       	for child in self.childs:
            ret += child.cal_cnt()
        self.cnt = ret
        return self.cnt

    def valid_solution(self, n):
        if not self.childs:
            return math.ceil(self.cnt / 3) <= n <= self.cnt
        sh = n // len(self.childs)
        rm = n % len(self.childs)
        for child in self.childs:
            if child.valid_solution(sh + (rm != 0)) == False:
                return False
            if rm:
                rm -= 1
        return True
    
    def make_seq(self, n):
        ret = []
        if not self.childs:
            ret = [1] * n
            cur = self.cnt - n
            for i in range(n-1, -1, -1):
                if cur == 0:
                    break
                if cur >= 2:
                    ret[i] += 2
                    cur -= 2
                else:
                    ret[i] += 1
                    cur -= 1
            return ret
        sh = n // len(self.childs)
        rm = n % len(self.childs)
        rst = []
        for child in self.childs:
            rst.append(child.make_seq(sh + (rm != 0)))
            if rm > 0:
                rm -= 1
        for i in range(sh):
            for lst in rst:
                ret.append(lst[i])
        for lst in rst:
            if len(lst) > sh:
                ret.append(lst[-1])
        return ret
            
def solution(edges, target):
    nodes = [Node(i) for i in range(len(target))]
    for p, c in edges:
        nodes[p-1].add_child(nodes[c-1])
    for i,cnt in enumerate(target):
        nodes[i].cnt = cnt
    root_cnt = nodes[0].cal_cnt()
    lo = math.ceil(root_cnt / 3)
    hi = root_cnt
    for cnt in range(lo, hi+1):
        if nodes[0].valid_solution(cnt):
            return nodes[0].make_seq(cnt)
    return [ -1 ]