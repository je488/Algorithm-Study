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
