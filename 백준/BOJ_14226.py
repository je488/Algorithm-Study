import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
sec = [[-1] * (n+1) for _ in range(n+1)]
Q = deque()
Q.append((1, 0))
sec[1][0] = 0
while Q:
    s, c = Q.popleft()
    if sec[s][s] == -1:
        sec[s][s] = sec[s][c] + 1
        Q.append((s, s))
    if s+c <= n and sec[s+c][c] == -1:
        sec[s+c][c] = sec[s][c] + 1
        Q.append((s+c, c))
    if s-1 >= 0 and sec[s-1][c] == -1:
        sec[s-1][c] = sec[s][c] + 1
        Q.append((s-1, c))
ans = -1
for i in range(n+1):
    if sec[n][i] != -1:
        if ans == -1 or ans > sec[n][i]:
            ans = sec[n][i]
print(ans)