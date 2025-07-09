import heapq
push = heapq.heappush
pop = heapq.heappop

def solution(jobs):
    pq = []
    rst = 0
    cur_time = 0
    cur_jobs = 0
    jobs.sort()
    def _push():
        nonlocal cur_jobs
        push(pq, (jobs[cur_jobs][1], jobs[cur_jobs][0], cur_jobs))
        cur_jobs += 1
    _push()
    while pq:
        t, req_time, _ = pop(pq)
        cur_time = max(cur_time, req_time)
        cur_time += t
        rst += cur_time - req_time
        while cur_jobs < len(jobs) and jobs[cur_jobs][0] <= cur_time:
            _push()
        if not pq and cur_jobs < len(jobs):
            _push()
    return(rst // len(jobs))
        