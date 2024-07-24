#dx, dy, dz는 6개의 인접한 방향으로 1씩 이동하기 위한 좌표
#d[i][j][k]의 값이 True이면 (i, j, k)에 정육면체가 놓여있음
#n, m, 종이 한 칸에 놓은 정육면체 수가 100 이하이므로 d배열의 크기는 100*100*100
#따라서 실제로 블럭을 3차원 배열에 채워보고 겉넓이를 계산해도 시간초과 발생X
#(x, y, z)칸에 대해 인접한 6개의 방향에 정육면체가 없는 칸이 나올 때마다 겉넓이 1 증가
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[[False] * 102 for j in range(102)] for i in range(102)]
for i in range(n):
    for j in range(m):
        for k in range(1, a[i][j]+1):
            d[i+1][j+1][k] = True
ans = 0
for x in range(1, n+1):
    for y in range(1, m+1):
        for z in range(1, a[x-1][y-1]+1):
            for k in range(6):
                nx, ny, nz = x+dx[k], y+dy[k], z+dz[k]
                if d[nx][ny][nz] == False:
                    ans += 1
print(ans)
