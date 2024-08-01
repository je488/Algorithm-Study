#빈 방 -> 빈 방은 부술 필요가 없으므로 가중치 0, 빈 방 -> 벽은 벽을 부숴야 하므로 가중치 1
#가중치가 0과 1이므로 큐를 2개로 분리(현재 큐, 다음 큐)
#현재 큐를 모두 방문하면 다음 큐가 현재 큐가 되고 새로운 비어있는 다음 큐 생성
#dx, dy는 오른쪽, 아래, 왼쪽, 위로 이동하기 위한 행과 열의 증가치
#dist[x][y]는 (x, y)로 이동하기 위해 벽을 부순 최소 횟수
#상하좌우로 인접한 방이 미로의 범위를 벗어나지 않고 이전에 방문하지 않은 경우 이동
#이동한 방이 빈 방이면 dist[xx][yy] = dist[x][y], 벽이면 dist[xx][yy] = dist[x][y] + 1
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
m, n = map(int, input().split())
a = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
Q = deque()
next_Q = deque()
Q.append((0, 0))
dist[0][0] = 0
while Q:
    x, y = Q.popleft()
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        if 0 <= xx < n and 0 <= yy < m and dist[xx][yy] == -1:
            if a[xx][yy] == 0:
                Q.append((xx, yy))
                dist[xx][yy] = dist[x][y]
            else:
                next_Q.append((xx, yy))
                dist[xx][yy] = dist[x][y] + 1
    if not Q:
        Q = next_Q
        next_Q = deque()
print(dist[n-1][m-1])
