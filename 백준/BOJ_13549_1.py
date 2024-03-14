import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 200000
check = [0] * MAX
dist = [-1] * MAX
n, m = map(int, input().split())
check[n] = 1
dist[n] = 0
Q = deque()
next_Q = deque()
Q.append(n)
while Q:
    now = Q.popleft()
    if now*2 < MAX and check[now*2] == 0:
        Q.append(now*2)
        check[now*2] = 1
        dist[now*2] = dist[now]
    if now-1 >= 0 and check[now-1] == 0:
        next_Q.append(now-1)
        check[now-1] = 1
        dist[now-1] = dist[now] + 1
    if now+1 < MAX and check[now+1] == 0:
        next_Q.append(now+1)
        check[now+1] = 1
        dist[now+1] = dist[now] + 1
    if not Q:
        Q = next_Q
        next_Q = deque()
print(dist[m])