import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * m for _ in range(n)]
def go(x, y, hap, cnt):
    global ans
    if cnt == 4:
        if ans < hap:
            ans = hap
        return
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if c[x][y]:
        return
    c[x][y] = True
    for d in range(4):
        go(x+dx[d], y+dy[d], hap+a[x][y], cnt+1)
    c[x][y] = False
ans = 0
for i in range(n):
    for j in range(m):
        go(i, j, 0, 0)
        if j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2]
            if i-1 >= 0:
                tmp2 = tmp + a[i-1][j+1]
                if ans < tmp2:
                    ans = tmp2
            if i+1 < n:
                tmp2 = tmp + a[i+1][j+1]
                if ans < tmp2:
                    ans = tmp2
        if i+2 < n:
            tmp = a[i][j] + a[i+1][j] + a[i+2][j]
            if j+1 < m:
                tmp2 = tmp + a[i+1][j+1]
                if ans < tmp2:
                    ans = tmp2
            if j-1 >= 0:
                tmp2 = tmp2 + a[i+1][j-1]
                if ans < tmp2:
                    ans = tmp2
print(ans)