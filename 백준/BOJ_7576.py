#토마토가 다 익기까지 걸리는 최소 일수를 구해야 하므로 BFS 이용
#dx, dy는 오른쪽, 아래, 왼쪽, 위로 이동하기 위한 행과 열의 증가치
#day는 방문 여부를 체크하고 익는 데 걸리는 일수를 기록하는 리스트
#day의 값이 -1이면 방문X, 0 이상이면 방문했고 익는 데 걸리는 일수 저장
#a를 탐색하면서 익은 토마토가 있으면 day의 값을 0으로 바꿔주고 큐에 좌표 넣기
#(xx, yy)가 상자의 범위를 벗어나지 않고 익지 않은 토마토이며 이전에 방문하지 않았으면 방문
#(xx, yy)의 토마토가 익는데 걸리는 일수는 (x, y)의 토마토가 익는데 걸리는 일수 + 1
#따라서 (x, y) -> (xx, yy)일 때 day[xx][yy] = day[x][y] + 1
#day의 값 중에서 가장 큰 값이 모든 토마토가 익는데 걸리는 최소 일수 -> max 이용하여 ans 구하기
#만약 익지 않은 토마토가 들어있던 좌표를 방문하지 않았다면 그 좌표의 토마토는 익지 않음
#따라서 토마토가 모두 익지 않았으므로 ans = -1
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
day = [[-1] * m for _ in range(n)]
Q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            day[i][j] = 0
            Q.append((i, j))

while Q:
    x, y = Q.popleft()
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        if 0 <= xx < n and 0 <= yy < m:
            if a[xx][yy] == 0 and day[xx][yy] == -1:
                day[xx][yy] = day[x][y] + 1
                Q.append((xx, yy))

ans = max([max(row) for row in day])
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and day[i][j] == -1:
            ans = -1
            break
print(ans)
