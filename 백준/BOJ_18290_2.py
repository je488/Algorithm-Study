#BOJ_18290_1.py에서 중복 선택을 방지하기 위해 이전에 선택한 칸의 행 번호 px 추가
#반복문에서 x는 px부터 시작 즉, 이전에 선택한 칸의 행부터 시작
#ex) (1, 2), (2, 1), (3, 4)를 선택 후 (2, 1), (1, 2), (3, 4)를 선택하는 경우 방지
#ex) (1, 2), (1, 5), (3, 4)를 선택 후 (1, 5), (1, 2), (3, 4)를 선택하는 경우 발생
#따라서 같은 행에서 중복된 선택 가능
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * m for _ in range(n)]
ans = -2147483647
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def go(px, cnt, s):
    if cnt == k:
        global ans
        if ans < s:
            ans = s
        return
    for x in range(px, n):
        for y in range(m):
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
                go(x, cnt + 1, s + a[x][y])
                c[x][y] = False
go(0, 0, 0)
print(ans)
