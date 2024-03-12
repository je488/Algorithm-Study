import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
Q = deque()
dist = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            dist[i][j] = 0
            Q.append((i, j))
while Q:
    x, y = Q.popleft()
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        if 0 <= xx < n and 0 <= yy < m:
            if a[xx][yy] == 0 and dist[xx][yy] == -1:
                Q.append((xx, yy))
                dist[xx][yy] = dist[x][y] + 1

ans = max([max(row) for row in dist])
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and dist[i][j] == -1:
            ans = -1
print(ans)