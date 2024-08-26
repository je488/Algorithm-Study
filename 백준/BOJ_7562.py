#나이트의 현재 위치에서 목표 위치까지 최소 이동 횟수를 구해야 하므로 BFS 이용
#dx, dy는 나이트가 이동할 수 있는 위치로 이동하기 위한 행과 열의 증가치
#dist는 방문 여부를 체크하고 이동 횟수를 저장하는 리스트
#dist의 값이 -1이면 방문X, 0 이상이면 방문했고 그 때의 이동 횟수 저장
#(xx, yy)가 체스판의 범위를 벗어나지 않고 이전에 방문하지 않은 경우 방문
#(x, y) -> (xx, yy)일 때 나이트의 위치에서 (xx, yy)까지 이동 횟수는 (x, y)까지 이동 횟수 + 1
#따라서 dist[xx][yy] = dist[x][y] + 1
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
T = int(input())
for _ in range(T):
    l = int(input())
    dist = [[-1] * l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    dist[sx][sy] = 0
    Q = deque()
    Q.append((sx, sy))
    while Q:
        x, y = Q.popleft()
        for d in range(8):
            xx = x + dx[d]
            yy = y + dy[d]
            if 0 <= xx < l and 0 <= yy < l and dist[xx][yy] == -1:
                Q.append((xx, yy))
                dist[xx][yy] = dist[x][y] + 1
    print(dist[ex][ey])
