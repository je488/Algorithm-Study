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