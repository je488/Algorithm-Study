import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
res = 0
Q = deque()
ch[n//2][n//2] = 1
res += li[n//2][n//2]
Q.append((n//2, n//2))
L = 0
while True:
    if L == n // 2:
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                res += li[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1
print(res)
