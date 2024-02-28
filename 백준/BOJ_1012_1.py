import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def DFS(x, y):
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        if 0 <= xx < m and 0 <= yy < n and a[xx][yy] == 1:
            a[xx][yy] = 0
            DFS(xx, yy)

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
                DFS(i, j)
                ans += 1
    print(ans)