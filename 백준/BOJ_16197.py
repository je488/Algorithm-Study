import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def go(step, x1, y1, x2, y2):
    if step == 11:
        return -1
    fall1 = fall2 = False
    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
        fall1 = True
    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
        fall2 = True
    if fall1 and fall2:
        return -1
    if fall1 or fall2:
        return step
    ans = -1
    for d in range(4):
        nx1, ny1 = x1 + dx[d], y1 + dy[d]
        nx2, ny2 = x2 + dx[d], y2 + dy[d]
        if 0 <= nx1 < n and 0 <= ny1 < m and a[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if 0 <= nx2 < n and 0 <= ny2 < m and a[nx2][ny2] == '#':
            nx2, ny2 = x2, y2
        tmp = go(step+1, nx1, ny1, nx2, ny2)
        if tmp == -1:
            continue
        if ans == -1 or ans > tmp:
            ans = tmp
    return ans

n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
x1 = y1 = x2 = y2 = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 'o':
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j
            a[i][j] = '.'
print(go(0, x1, y1, x2, y2))