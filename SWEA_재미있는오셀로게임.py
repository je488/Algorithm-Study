#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQmA4uK8ygDFAXj(문제링크)
#돌을 놓을 때마다 나와 같은색 돌 사이에 있는 다른색 돌들을 모두 뒤집기
#돌을 놓을 위치와 색이 주어지면 상하좌우와 대각선을 탐색하며 뒤집을 돌들을 찾아 뒤집기
#dx, dy는 board에서 →, ↓, ←, ↑, ↗, ↘, ↙, ↖ 방향을 탐색하기 위한 행과 열의 인덱스 증가치
#change는 뒤집어야 할 돌들의 위치를 저장한 리스트
#상하좌우 및 대각선으로 탐색중인 좌표가 경계선을 넘는 경우 change 리스트를 비우고 break
#좌표에 해당하는 돌이 같은색이면 좌표 전까지 change에 저장된 돌들만 뒤집으면 되므로 break
#좌표가 0으로 비어있는 경우 change 리스트를 비우고 break
#좌표가 경계선을 넘지 않고 비어있지 않고 같은색이 아니면 뒤집어야할 돌이므로 change에 저장
#while 반복문이 종료되면 change에 저장된 위치에 해당하는 돌의 색을 주어진 색(c)으로 뒤집기
#board를 탐색하며 흑돌의 개수(b_cnt)와 백돌의 개수(w_cnt) 구하기
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
