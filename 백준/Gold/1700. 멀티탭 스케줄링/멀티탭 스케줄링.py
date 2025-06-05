import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
jobs = list(map(int, input().split()))
job_idx = {}
for i, job in enumerate(jobs):
    if job in job_idx:
        job_idx[job].append(i)
    else:
        job_idx[job] = deque([i])

def plug_out(pluged):
    farther_idx = 0
    pluged_idx = 0
    for pi, ji in enumerate(pluged):
        if not job_idx[ji]:
            del(pluged[pi])
            return
        elif farther_idx < job_idx[ji][0]:
            farther_idx = job_idx[ji][0]
            pluged_idx = pi
    del(pluged[pluged_idx])

def plug_in(pluged, tar_job_idx):
    job = jobs[tar_job_idx]
    pluged.append(job)
    job_idx[job].popleft()

pluged = []
cur_job = 0
rst = 0
while cur_job < k:
    if jobs[cur_job] not in pluged:
        if len(pluged) == n:
            rst += 1
            plug_out(pluged)
        plug_in(pluged, cur_job)
    else:
        job_idx[jobs[cur_job]].popleft()
    cur_job += 1
print(rst)
