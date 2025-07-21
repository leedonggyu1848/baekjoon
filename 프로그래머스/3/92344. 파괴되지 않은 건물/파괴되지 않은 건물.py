def solution(board, skill):
    sy = len(board)
    sx = len(board[0])
    acc = [[0] * (sx+1) for _ in range(sy+1)]
    for t, y1, x1, y2, x2, degree in skill:
        dmg = -degree if t == 1 else degree
        acc[y1][x1] += dmg
        acc[y1][x2+1] -= dmg
        acc[y2+1][x1] -= dmg
        acc[y2+1][x2+1] += dmg
    for y in range(sy):
        for x in range(sx):
            acc[y][x+1] += acc[y][x]
            
    for x in range(sx):
        for y in range(sy):
            acc[y+1][x] += acc[y][x]
    
    rst = 0
    for y in range(sy):
        for x in range(sx):
            if board[y][x] + acc[y][x] > 0:
                rst += 1
                
    return rst
