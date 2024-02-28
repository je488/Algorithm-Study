import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def BFS(x, y):
    Q = deque()
    Q.append((x, y))
    while Q:
        tmp = Q.popleft()
        for d in range(4):
            xx = tmp[0] + dx[d]
            yy = tmp[1] + dy[d]
            if 0 <= xx < m and 0 <= yy < n and a[xx][yy] == 1:
                a[xx][yy] = 0
                Q.append((xx, yy))
T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    a = [[0] * n for _ in range(m)]
    ans = 0
    for _ in range(k):
        x, y = map(int, input().split())
        a[x][y] = 1
    for i in range(m):
        for j in range(n):
            if a[i][j] == 1:
                a[i][j] = 0
                BFS(i, j)
                ans += 1
    print(ans)