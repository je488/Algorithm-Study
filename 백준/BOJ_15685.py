import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
c = [[False] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
def curve(dir, gen):
    ans = [dir]
    for _ in range(1, gen+1):
        tmp = ans[:]
        tmp = tmp[::-1]
        for i in range(len(tmp)):
            tmp[i] = (tmp[i]+1) % 4
        ans += tmp
    return ans

n = int(input())
for _ in range(n):
    y, x, dir, gen = map(int, input().split())
    dirs = curve(dir, gen)
    c[x][y] = True
    for d in dirs:
        x += dx[d]
        y += dy[d]
        c[x][y] = True
ans = 0
for i in range(100):
    for j in range(100):
        if c[i][j] and c[i][j+1] and c[i+1][j] and c[i+1][j+1]:
            ans += 1
print(ans)