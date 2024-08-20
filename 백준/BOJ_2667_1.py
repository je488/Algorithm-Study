#dx, dy는 a에서 오른쪽, 아래, 왼쪽, 위를 탐색하기 위한 행과 열의 증가치
#group은 방문 여부를 판단하는 리스트로 방문하지 않았으면 0, 방문했으면 단지 번호(cnt)
#현위치에서 상하좌우로 인접한 xx, yy가 정사각형의 범위 안이고 이전에 방문하지 않은 경우 이동
#reduce 함수를 이용하여 group을 1차원 리스트로 변경한 후 값이 0보다 큰 경우에만 ans에 저장
#Counter를 이용하여 단지별 집의 개수를 구한 뒤 오름차순으로 정렬하여 ans에 저장
#cnt는 새로운 단지를 발견한 경우에만 1 증가하므로 cnt는 단지 수와 같음
import sys
from functools import reduce
from collections import Counter
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def DFS(x, y, cnt):
    group[x][y] = cnt
    for d in range(4):
        xx, yy = x + dx[d], y + dy[d]
        if 0 <= xx < n and 0 <= yy < n:
            if a[xx][yy] == 1 and group[xx][yy] == 0:
                DFS(xx, yy, cnt)

n = int(input())
a = [list(map(int, input().rstrip())) for _ in range(n)]
group = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            DFS(i, j, cnt)

ans = reduce(lambda x, y : x+y, group)
ans = [x for x in ans if x > 0]
ans = sorted(list(Counter(ans).values()))
print(cnt)
print('\n'.join(map(str, ans)))
