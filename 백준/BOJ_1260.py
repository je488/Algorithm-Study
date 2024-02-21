import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, start = map(int, input().split())
a = [[] for _ in range(n+1)]
check = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(1, n+1):
    a[i].sort()

def DFS(x):
    check[x] = 1
    print(x, end = ' ')
    for y in a[x]:
        if check[y] == 0:
            DFS(y)

def BFS(s):
    check = [0] * (n+1)
    Q = deque()
    Q.append(s)
    check[s] = 1
    while Q:
        x = Q.popleft()
        print(x, end = ' ')
        for y in a[x]:
            if check[y] == 0:
                check[y] = 1
                Q.append(y)

DFS(start)
print()
BFS(start)
print()