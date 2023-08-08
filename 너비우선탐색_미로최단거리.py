#(0, 0)부터 상하좌우 4개의 가지로 뻗어나감
#dx, dy는 격자판(li)에서 오른쪽, 아래, 왼쪽, 위를 탐색하기 위한 행과 열의 인덱스 증가치
#dis의 인덱스가 좌표 지점, dis의 값은 출발점에서 좌표 지점까지 가는데 이동한 최소횟수
#ch를 따로 생성하는 대신 li의 값으로 방문여부 표시(방문하면 값을 1(벽)로 바꿔주기)
#큐에 노드를 넣을 때 좌표가 0부터 6사이에 있는지 확인하고 방문한 적이 없는지(벽이 아닌지) 체크
#출발점에서 부모 노드까지 이동한 횟수 + 1 -> 출발점에서 자식 노드까지 이동한 횟수
#dis[6][6]의 값이 0이면 (6,6)까지 도달하지 못했으므로 -1 출력
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
li = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]
Q = deque()
Q.append((0, 0))
li[0][0] = 1
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and li[x][y] == 0:
            li[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            Q.append((x, y))
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])
