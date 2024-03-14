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