#종이 한 칸에 놓은 정육면체 수가 1 이상이므로 윗 면과 아랫 면의 넓이는 항상 n*m
#따라서 ans = 2*n*m으로 두고 옆 면의 넓이를 구하여 더하기
#옆 면의 넓이는 인접한 높이의 차이로 구하기
#위, 아래를 제외하면 행과 열의 차이이므로 BOJ_16931_1.py와 달리 dx, dy만 필요
#(x, y)칸이 있을 때 인접한 (nx, ny)칸보다 높이가 크거나 같은 경우에만 높이의 차이를 ans에 더하기
#인접한 방향에 정육면체가 없으면 현재 높이를 그대로 ans에 더해야 하므로 a 주위를 0으로 채우기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a = [[0] * (m+2)] + [[0] + row + [0] for row in a] + [[0] * (m+2)]
ans = 2*n*m
for x in range(1, n+1):
    for y in range(1, m+1):
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if a[x][y] - a[nx][ny] >= 0:
                ans += a[x][y] - a[nx][ny]
print(ans)
