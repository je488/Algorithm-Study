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
