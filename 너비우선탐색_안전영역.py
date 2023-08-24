#주어진 높이 정보에서 최댓값을 찾아 비의 양이 0부터 최댓값-1일 때 각각 안전영역의 개수 세기
#비의 양이 최댓값이면 모두 잠겨 안전영역의 개수가 0이므로 최댓값-1까지만 반복
#안전영역의 개수를 세기 위해 li에서 값이 비의 양보다 크고 이전에 방문한 적이 없는 좌표 찾기
#찾은 좌표를 기준으로 상하좌우 탐색 -> 4개의 가지로 뻗어나감
#dx, dy는 li에서 오른쪽, 아래, 왼쪽, 위를 탐색하기 위한 행과 열의 인덱스 증가치
#ch는 중복 방문하지 않기 위해 방문여부를 체크하는 리스트 -> 비의 양이 바뀔 때마다 초기화
#큐에 노드를 넣을 때 좌표가 경계선을 넘지 않고 방문한 적이 없고 li의 값이 비의 양보다 큰지 확인
#큐가 비면 한 개의 안전영역을 모두 탐색한 것이므로 cnt(안전영역의 수) += 1
#안전영역의 개수가 이전에 구한 안전영역의 최대 개수(res)보다 크면 res값을 cnt로 바꿔주기
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
maxv = -2147000000
res = 0
for i in li:
    if maxv < max(i):
        maxv = max(i)
for rain in range(maxv):
    cnt = 0
    Q = deque()
    ch = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if li[j][k] > rain and ch[j][k] == 0:
                Q.append((j, k))
                ch[j][k] = 1
                while Q:
                    tmp = Q.popleft()
                    for d in range(4):
                        x = tmp[0] + dx[d]
                        y = tmp[1] + dy[d]
                        if 0<=x<n and 0<=y<n and li[x][y] > rain and ch[x][y] == 0:
                            Q.append((x, y))
                            ch[x][y] = 1
                cnt += 1
    if res < cnt:
        res = cnt
print(res)
