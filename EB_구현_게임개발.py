import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
x, y, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ch[x][y] = 1
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3
res = 1
turn = 0
while True:
    turn_left()
    a = x + dx[d]
    b = y + dy[d]
    if ch[a][b] == 0 and map[a][b] == 0:
        ch[a][b] = 1
        x, y = a, b
        res += 1
        turn = 0
        continue
    else:
        turn += 1
    if turn == 4:
        a = x - dx[d]
        b = y - dy[x]
        if map[a][b] == 0:
            x, y = a, b
        else:
            break
        turn = 0
print(res)
