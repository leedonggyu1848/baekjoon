import sys
sys.setrecursionlimit(10**6)
slots = {}

def find_slot(req):
    if not req in slots:
        return req
    slots[req] = find_slot(slots[req])
    return slots[req]

def request_slot(req):
    ret = find_slot(req)
    slots[ret] = ret + 1
    return ret
        
def solution(k, room_number):
    return [request_slot(i) for i in room_number]