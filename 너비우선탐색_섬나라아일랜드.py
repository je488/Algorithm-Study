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
