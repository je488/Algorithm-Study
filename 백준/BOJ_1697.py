import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 200000
check = [0] * (MAX+1)
sec = [-1] * (MAX+1)
n, k = map(int, input().split())
Q = deque()
Q.append(n)
check[n] = 1
sec[n] = 0
while Q:
    now = Q.popleft()
    for nxt in [now+1, now-1, now*2]:
        if 0 <= nxt <= MAX and check[nxt] == 0:
            check[nxt] = 1
            sec[nxt] = sec[now] + 1
            Q.append(nxt)
print(sec[k])
