A = False
B = True

def is_left_win(t, left, right):
    # A 기준
    if left[0] != right[0]:  # 승패가 정해짐
        rst = left[0]
    elif left[0]: # 무조건 승리함
        rst = left[1] < right[1]
    else: # 무조건 패배함
        rst = left[1] > right[1]
    return rst if t == A else not rst

def solution(board, aloc, bloc):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    def is_range(y, x):
        return 0 <= y < len(board) and 0 <= x < len(board[0])

    def dfs(move, stop, turn):
        nonlocal board
        if board[move[0]][move[1]] == 0:
            return (turn, 0) # a가 패배
        rst = None
        factor = None
        for i in range(4):
            y = move[0] + dy[i]
            x = move[1] + dx[i]
            if not is_range(y, x):
                continue
            if board[y][x] == 0:
                continue
            board[move[0]][move[1]] = 0
            factor = dfs(stop, (y, x), not turn)
            board[move[0]][move[1]] = 1
            if rst == None or is_left_win(turn, factor, rst):
                rst = factor
        if rst == None:
            return (turn, 0) # (A가 이기나?, turn수)
        if move == stop:
            return (not turn, 1)
        else:
            return(rst[0], rst[1]+1)

    return dfs(aloc, bloc, A)[1]
