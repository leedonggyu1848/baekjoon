import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def simplify(edges):
    ids = [-1] * (nv)
    finished = [False] * (nv)
    nxt_id = 0
    s = []
    groups = [-1] * (nv)
    sccs = []
    group_id = 0
    
    def dfs(cur):
        nonlocal nxt_id, group_id
        ids[cur] = nxt_id
        pcur = nxt_id
        nxt_id += 1
        s.append(cur)
        ret = []

        for nxt in edges[cur]:
            if ids[nxt] == -1: # 방문한 적 없음
                pcur = min(pcur, dfs(nxt)) # 방문
            elif not finished[nxt]: # 방문했지만 스택안에 존재(진행중)
                pcur = min(pcur, ids[nxt]) # 바로 업데이트
        if pcur == ids[cur]: # 내가 scc의 시작지점
            scc = []
            while s:
                emt = s.pop()
                scc.append(emt)
                finished[emt] = True
                groups[emt] = group_id
                if emt == cur:
                    break
            sccs.append(scc)
            group_id += 1
        return pcur

    for cur in range(nv):
        if not finished[cur]:
            dfs(cur)

    return sccs, groups

for _ in range(int(input())):
    nv, ne = map(int, input().split())
    edges = [[] for _ in range(nv)]
    for _ in range(ne):
        s, e = map(int, input().split())
        s -= 1
        e -= 1
        edges[s].append(e)
    sccs, groups = simplify(edges)
    indegrees = [0 for _ in range(len(sccs))]
    for s, edge in enumerate(edges):
        for e in edge:
            s_group = groups[s]
            e_group = groups[e]
            if s_group != e_group:
                indegrees[e_group] += 1
    rst = 0
    for indegree in indegrees:
        if indegree == 0:
            rst += 1
    print(rst)