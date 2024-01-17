#2차원 리스트 a를 1차원 리스트라고 가정해서 문제 풀기
#(i, j)는 i * m + j로 표현 -> row-major order
#ex) a가 3*4인 경우 a[0][0] -> 0, a[0][1] -> 1, ..., a[1][0] -> 4, ..., a[2][3] -> 11
#반복문에서 j는 prev + 1(이전에 선택한 칸 + 1)부터 시작하고 n * m 전까지
#칸의 x좌표는 j // m, y좌표는 j % m
#재귀 함수 호출 시, 현재 칸의 좌표를 1차원 리스트의 좌표처럼 표현한 x * m + y를 인자로 넘기기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * m for _ in range(n)]
ans = -2147483647
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def go(prev, cnt, s):
    if cnt == k:
        global ans
        if ans < s:
            ans = s
        return
    for j in range(prev+1, n*m):
        x = j // m
        y = j % m
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
            go(x*m+y, cnt + 1, s + a[x][y])
            c[x][y] = False
go(-1, 0, 0)
print(ans)
