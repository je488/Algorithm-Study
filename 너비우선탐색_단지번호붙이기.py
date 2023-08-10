#깊이우선탐색_단지번호붙이기와 같은 문제
#li에서 값이 1인 좌표를 찾고 상하좌우 4개의 가지로 뻗어나감
#dx, dy는 li에서 오른쪽, 아래, 왼쪽, 위를 탐색하기 위한 행과 열의 인덱스 증가치
#cnt는 단지별 집의 개수로 li의 행과 열을 탐색하면서 집을 발견하면 1로 초기화
#이미 방문한 곳은 다시 방문하지 않기 위해 li의 값을 0으로 변경
#큐에 노드를 넣을 때 좌표과 0과 n-1 사이인지, li의 값이 1(집)인지 확인
#Q가 비면 하나의 단지를 모두 탐색한 것이므로 집의 개수를 ans에 추가하고 오름차순으로 출력
#하나의 단지를 모두 탐색했을 때 ans에 추가하므로 총 단지수는 ans의 길이와 같음
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1 ,0]
n = int(input())
li = [list(map(int, input().rstrip())) for _ in range(n)]
ans = list()
Q = deque()
for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            Q.append((i, j))
            li[i][j] = 0
            cnt = 1
            while Q:
                tmp = Q.popleft()
                for k in range(4):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0<=x<=n-1 and 0<=y<=n-1 and li[x][y] == 1:
                        li[x][y] = 0
                        cnt += 1
                        Q.append((x, y))
            ans.append(cnt)
print(len(ans))
for a in sorted(ans):
    print(a)
