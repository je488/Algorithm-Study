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
