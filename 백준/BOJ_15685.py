#드래곤 커브를 만들고 4개의 꼭지점이 드래곤 커브의 일부인 정사각형 개수 구하기
#드래곤 커브에 대한 정보를 시작점의 좌표와 방향으로 기록
#i세대에서 i+1세대의 드래곤 커브 만드는 방법
#1. i세대의 방향의 순서를 반대로 하기
#2. 방향을 반시계 방향으로 90도 회전
#3. 회전한 방향을 i세대에 붙여주기
#ex) 1세대에서 2세대 드래곤 커브 만들기
#ex) 1세대는 방향이 → ↑ 이므로 순서를 반대로 하면 ↑ →
#ex) 방향을 반시계 방향으로 90도 회전하면 ← ↑
#ex) 1세대에 회전한 방향을 붙여주면 → ↑ ← ↑(2세대 드래곤 커브)
#curve는 gen세대 드래곤 커브의 방향을 만드는 함수
#dx, dy는 순서대로 → ↑ ← ↓ 방향으로 이동하기 위한 행과 열의 증가치
#→(0) ↑(1) ←(2) ↓(3)을 반시계 방향으로 90도 회전하면 ↑(1) ←(2) ↓(3) →(0)
#따라서 반시계 방향으로 회전하면 (현재 방향 + 1) % 4
#c는 꼭지점이 드래곤 커브의 일부인지 체크하기 위한 리스트
#(i, j)가 드래곤 커브에 포함되는 꼭지점이면 c[i][j]는 True, 포함되지 않으면 False
#curve에서 만든 드래곤 커브의 방향을 바탕으로 드래곤 커브의 꼭지점을 찾아 c값을 True로 변경
#0부터 100까지 인접한 4개의 꼭지점(정사각형)이 모두 드래곤 커브에 포함되어 있는지 확인
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
