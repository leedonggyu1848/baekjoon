import math

def cal_cost(target):
    A = 0
    Z = ord('Z') - ord('A')
    tar = ord(target) - ord('A')
    up = tar - A
    down = Z - tar + 1
    return min(up, down)

def cal_right_dist(tar):
    src = 0
    if src == tar:
        return 0
    ret = 0
    while src != tar-1:
        ret += 1
        src += 1
    return ret

def cal_left_dist(tar, n):
    src = 0
    if src == tar:
        return 0
    ret = 0
    src = n-1
    ret += 1
    while src != tar:
        src -= 1
        ret += 1
    ret -= 1
    return ret


def solution(name):
    costs = []
    for c in name:
        costs.append(cal_cost(c))
    rst = sum(costs)
    s_right = -1
    s_left = math.inf
    for i, c in enumerate(costs):
        if c != 0:
            s_right = max(s_right, i)
            s_left = min(s_left, i)
    if s_right == -1:
        return rst
    s_left = len(costs) - s_left
    points = []
    cur_start = -1
    max_len = 0
    is_0seq = False
    for i, c in enumerate(costs):
        if c == 0 and not is_0seq:
            is_0seq = True
            cur_start = i
        if c != 0 and is_0seq:
            is_0seq = False
            if max_len < i - cur_start:
                points = []
            if max_len <= i - cur_start:
                max_len = i - cur_start
                points.append((cur_start, i - 1))
            cur_start = -1
    if cur_start != -1:
        if max_len < len(costs) - cur_start:
            points = []
        if max_len <= len(costs) - cur_start:
            max_len = len(costs) - cur_start
            points.append((cur_start, len(costs) - 1))

    if points:
        right_turn = cal_right_dist(points[0][0]) * 2 + cal_left_dist(points[0][1], len(costs))
        left_turn = cal_left_dist(points[-1][1], len(costs))*2 + cal_right_dist(points[-1][0])
        return rst + min(s_left, s_right, right_turn, left_turn)

    return rst + min(s_left, s_right)
