from collections import deque

V = 0
H = 1

def fill_virtical(board, x):
    for _y in range(0, len(board)):
        if board[_y][x] > 0:
            return
        board[_y][x] = -1

def get_block_group(board, tars):
    slots = {}
    for y, x in tars:
        if board[y][x] > 0:
            slots[board[y][x]] = slots.get(board[y][x], 0)+1
    for k, v in slots.items():
        if v == 4:
            return k
    return None

def make_targets(y, x, t):
    if t == V:
        return [(_y, _x) for _y in range(y, y+3) for _x in range(x, x+2)]
    else:
        return [(_y, _x) for _y in range(y, y+2) for _x in range(x, x+3)]


def get_v_block(board, y, x):
    if y+3 > len(board) or x+2 > len(board[0]):
        return None
    group = get_block_group(board, make_targets(y, x, V))
    if group:
        return (y, x, group, V)
    return None


def get_h_block(board, y, x):
    if y+2 > len(board) or x+3 > len(board[0]):
        return None
    group = get_block_group(board, make_targets(y, x, H))
    if group:
        return (y, x, group, H)
    return None

def can_remove(board, block):
    sy, sx, group, t = block
    cnt = 0
    for y, x in make_targets(sy, sx, t):
        if board[y][x] == group or board[y][x] == -1:
            continue
        return False
    return True

def remove_block(board, block):
    sy, sx, group, t = block
    for y, x in make_targets(sy, sx, t):
        board[y][x] = 0
    for x in range(sx, sx + (2 if t == V else 3)):
        fill_virtical(board, x)

def solution(board):
    for x in range(len(board[0])):
        if board[0][x] == 0:
            fill_virtical(board, x)
    blocks = deque()
    for y in range(len(board)):
        for x in range(len(board[0])):
            block = get_v_block(board, y, x)
            if block:
                blocks.append(block)
            block = get_h_block(board, y, x)
            if block:
                blocks.append(block)
    rst = 0
    num_blocks = len(blocks)
    cnt_blocks = 0
    while blocks:
        if cnt_blocks >= num_blocks:
            break
        block = blocks.pop()
        if can_remove(board, block):
            remove_block(board, block)
            rst += 1
            cnt_blocks = 0
            num_blocks -= 1
        else:
            blocks.appendleft(block)
            cnt_blocks += 1
    return rst
