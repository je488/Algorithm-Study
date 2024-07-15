#ㅜ모양을 제외한 나머지 모양은 어떤 한 위치에서 시작해 연속하고 인접하는 3개의 칸을 방문한 모양
#ㅜ모양을 제외한 나머지 모양은 재귀 함수 이용, ㅜ모양은 for문 이용
#c는 중복 방문하지 않기 위해 방문 여부를 체크하는 리스트
#dx, dy는 오른쪽, 아래, 왼쪽, 위를 탐색하기 위한 행과 열의 증가치
#hap은 현재까지 칸에 써있는 수의 합
#cnt는 방문한 칸의 개수
#cnt == 4이면 정답을 찾은 경우이므로 현재까지 구한 정답과 비교해서 최대값 구하기
#칸이 범위를 벗어나면 return
#종이에 여러가지 모양을 놓기 위해서는 같은 칸을 여러 번 사용할 수 있어야 함
#따라서 go 함수를 호출한 뒤에 c[x][y]의 값을 True에서 False로 다시 바꿔주기
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
