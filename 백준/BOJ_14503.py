#dx, dy는 순서대로 북, 동, 남, 서 방향으로 한칸 이동하기 위한 행과 열의 증가치
#a의 값이 0이면 청소하지 않은 칸, 1이면 벽, 2면 청소한 칸
#현재 위치가 청소되어 있지 않으면(a의 값이 0이면) 청소하기(a의 값을 2로 바꾸기)
#현재 위치에서 네 방향이 모두 청소가 되어있거나 벽이면(즉, 0이 아니면) 뒤쪽 방향 확인
#현재 청소기가 보고 있는 방향이 dir이므로 뒤쪽 방향의 좌표는 x-dx[dir], y-dy[dir]
#뒤쪽 방향이 벽이면 작동을 중지(break)하고, 벽이 아니면 후진
#네 방향 중 한 방향이라도 청소가 안되어있으면 반시계 방향으로 90도 회전
#북(0), 동(1), 남(2), 서(3)에서 반시계 방향으로 회전하면 서(3), 북(0), 동(1), 남(2)
#따라서 (dir + 3) % 4로 방향 회전
#회전한 방향에 청소하지 않은 칸이 있다면 그 방향으로 한 칸 전진
#작동이 중지된 뒤에 모든 칸을 탐색하면서 청소한 칸의 수 세기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
x, y, dir = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
while True:
    if a[x][y] == 0:
        a[x][y] = 2
    if a[x+1][y] != 0 and a[x-1][y] != 0 and a[x][y+1] != 0 and a[x][y-1] != 0:
        if a[x-dx[dir]][y-dy[dir]] == 1:
            break
        else:
            x -= dx[dir]
            y -= dy[dir]
    else:
        dir = (dir + 3) % 4
        if a[x+dx[dir]][y+dy[dir]] == 0:
            x += dx[dir]
            y += dy[dir]
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            cnt += 1
print(cnt)
