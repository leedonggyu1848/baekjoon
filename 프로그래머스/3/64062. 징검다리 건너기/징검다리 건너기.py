import heapq
push = heapq.heappush
pop = heapq.heappop

def solution(stones, k):
    pq = []
    for i in range(k):
        push(pq, (-stones[i], i))
        
    for cur in range(k, len(stones)):
        v, _ = pq[0]
        v = -v
        nv = min(stones[cur], v)
        while pq and pq[0][1] <= cur - k:
            pop(pq)
        push(pq, (-nv, cur))
        
    return -pq[0][0]