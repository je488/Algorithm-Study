#BOJ_18290_2.py에서 같은 행에서 중복된 선택을 하는 경우를 방지하기 위해 py 추가
#(px, py)는 이전에 선택한 칸의 좌표
#반복문에서 x는 px(이전에 선택한 칸의 행)부터 시작
#y는 px == x인 경우 py(이전에 선택한 칸의 열)부터 시작하고 px > x인 경우 0부터 시작
#정확하게는 px == x인 경우 py + 1부터 시작이지만 if (c[x][y]):에서 걸리므로 py부터 시작
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * m for _ in range(n)]
ans = -2147483647
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def go(px, py, cnt, s):
    if cnt == k:
        global ans
        if ans < s:
            ans = s
        return
    for x in range(px, n):
        for y in range(py if x == px else 0, m):
            if c[x][y]:
                continue
            ok = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if c[nx][ny]:
                        ok = False
            if ok:
                c[x][y] = True
                go(x, y, cnt + 1, s + a[x][y])
                c[x][y] = False
go(0, 0, 0, 0)
print(ans)
