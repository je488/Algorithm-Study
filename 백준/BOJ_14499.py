import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n, m, x, y, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))
dice = [0] * 7
for k in move:
    k -= 1
    nx, ny = x + dx[k], y + dy[k]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    if k == 0:
        tmp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = tmp
    elif k == 1:
        tmp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = tmp
    elif k == 2:
        tmp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = tmp
    else:
        tmp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = tmp
    x, y = nx, ny
    if a[x][y] == 0:
        a[x][y] = dice[6]
    else:
        dice[6] = a[x][y]
        a[x][y] = 0
    print(dice[1])