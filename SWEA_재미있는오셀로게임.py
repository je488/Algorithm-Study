import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    s = n//2
    board[s][s] = 2
    board[s-1][s-1] = 2
    board[s][s-1] = 1
    board[s-1][s] = 1
    for _ in range(m):
        b, a, c = map(int, input().split())
        x = a - 1
        y = b - 1
        board[x][y] = c
        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]
            change = list()
            while True:
                if 0 <= xx < n and 0 <= yy < n:
                    if board[xx][yy] == 0:
                        change.clear()
                        break
                    elif board[xx][yy] == c:
                        break
                    else:
                        change.append((xx, yy))
                else:
                    change.clear()
                    break
                xx += dx[i]
                yy += dy[i]
            for xx, yy in change:
                board[xx][yy] = c
    b_cnt, w_cnt = 0, 0
    for b in board:
        b_cnt += b.count(1)
        w_cnt += b.count(2)
    print(f'#{tc} {b_cnt} {w_cnt}')


