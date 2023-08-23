#li에서 값이 1인 좌표를 찾고 상하좌우와 대각선 총 8개의 가지로 뻗어나감
#dx, dy는 li에서 →, ↓, ←, ↑, ↗, ↘, ↙, ↖ 방향을 탐색하기 위한 행과 열의 인덱스 증가치
#이미 방문한 곳은 다시 방문하지 않기 위해 li의 값을 0으로 변경
#큐에 노드를 넣을 때 좌표가 0보다 크거나 같고 n보다 작은지, li의 값이 1인지 확인
#큐가 비면 하나의 섬을 모두 탐색한 것이므로 res(섬의 개수)에 +1
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1, -1, 1, 1, -1]
dy = [1, 0, -1, 0, 1, 1, -1, -1]
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
Q = deque()
res = 0
for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            Q.append((i, j))
            li[i][j] = 0
            while Q:
                tmp = Q.popleft()
                for d in range(8):
                    x = tmp[0] + dx[d]
                    y = tmp[1] + dy[d]
                    if 0 <= x < n and 0 <= y < n and li[x][y] == 1:
                        Q.append((x, y))
                        li[x][y] = 0
            res += 1
print(res)
