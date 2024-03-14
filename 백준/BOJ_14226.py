import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
dist = [[-1] * (n+1) for _ in range(n+1)]
Q = deque()
Q.append((1, 0))
dist[1][0] = 0
while Q:
    s, c = Q.popleft()
    if dist[s][s] == -1:
        dist[s][s] = dist[s][c] + 1
        Q.append((s, s))
    if s+c <= n and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1
        Q.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        Q.append((s-1, c))
ans = -1
for i in range(n+1):
    if dist[n][i] != -1:
        if ans == -1 or ans > dist[n][i]:
            ans = dist[n][i]
print(ans)