import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def DFS(x, y):
    global res
    if x == ex and y == ey:
        res += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and li[x][y] < li[xx][yy]:
                DFS(xx, yy)

if __name__ == "__main__":
    res = 0
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    maxv, minv = -2147000000, 2147000000
    for i in range(n):
        for j in range(n):
            if li[i][j] > maxv:
                maxv = li[i][j]
                ex = i
                ey = j
            if li[i][j] < minv:
                minv = li[i][j]
                sx = i
                sy = j
    DFS(sx, sy)
    print(res)
