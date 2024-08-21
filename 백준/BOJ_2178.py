#(1, 1)에서 (N, M)으로 가는 최단 경로를 구해야 하므로 BFS 이용
#코드에서는 출발점을 (0, 0)로 설정하여 (0, 0)에서 (N-1, M-1)로 가는 최단 경로를 구함
#dx, dy는 오른쪽, 아래, 왼쪽, 위로 이동하기 위한 행과 열의 증가치
#dist는 방문 여부를 체크하고 거리를 기록하는 리스트
#dist의 값이 -1이면 방문X, 0 이상이면 방문했고 그 때의 거리 저장
#(xx, yy)가 미로의 범위를 벗어나지 않고 이동할 수 있으며 이전에 방문하지 않은 경우 방문
#(x, y) -> (xx, yy)일 때 (xx, yy)까지의 거리는 (x, y)까지의 거리 + 1
#따라서 dist[xx][yy] = dist[x][y] + 1
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
a = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
Q = deque()
Q.append((0, 0))
dist[0][0] = 1
while Q:
    x, y = Q.popleft()
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        if 0 <= xx < n and 0 <= yy < m:
            if dist[xx][yy] == -1 and a[xx][yy] == 1:
                Q.append((xx, yy))
                dist[xx][yy] = dist[x][y] + 1
print(dist[n-1][m-1])
