#큐 대신 덱(deque) 사용 -> 큐와 달리 덱은 양쪽에서 값을 넣고 빼는 것이 가능
#벽을 부수지 않는 경우(빈 방)는 덱의 앞에, 벽을 부수는 경우(벽)는 덱의 뒤에 넣기
#BOJ_1261_1.py에서 현재 큐에 넣은 것을 덱의 앞에, 다음 큐에 넣은 것을 덱의 뒤에 넣기
#덱이 비어있으면 반복문 종료
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
m, n = map(int, input().split())
a = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
Q = deque()
Q.append((0, 0))
dist[0][0] = 0
while Q:
    x, y = Q.popleft()
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        if 0 <= xx < n and 0 <= yy < m and dist[xx][yy] == -1:
            if a[xx][yy] == 0:
                Q.appendleft((xx, yy))
                dist[xx][yy] = dist[x][y]
            else:
                Q.append((xx, yy))
                dist[xx][yy] = dist[x][y] + 1
print(dist[n-1][m-1])
