import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 200000
sys.setrecursionlimit(MAX)
check = [0] * (MAX+1)
sec = [-1] * (MAX+1)
via = [-1] * (MAX+1)
n, k = map(int, input().split())
check[n] = 1
sec[n] = 0
Q = deque()
Q.append(n)
while Q:
    now = Q.popleft()
    for nxt in [now+1, now-1, now*2]:
        if 0 <= nxt < MAX and check[nxt] == 0:
            check[nxt] = 1
            sec[nxt] = sec[now] + 1
            via[nxt] = now
            Q.append(nxt)
print(sec[k])
def go(n, k):
    if n != k:
        go(n, via[k])
    print(k, end=' ')
go(n, k)