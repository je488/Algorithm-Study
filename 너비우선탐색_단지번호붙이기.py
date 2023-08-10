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
                    if 0<=x<n and 0<=y<n and li[x][y] == 1:
                        li[x][y] = 0
                        cnt += 1
                        Q.append((x, y))
            ans.append(cnt)
print(len(ans))
for a in sorted(ans):
    print(a)
