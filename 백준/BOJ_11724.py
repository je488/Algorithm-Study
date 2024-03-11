import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
check = [False] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

def DFS(x):
    check[x] = True
    for y in a[x]:
        if check[y] == False:
            DFS(y)

ans = 0
for i in range(1, n+1):
    if not check[i]:
        DFS(i)
        ans += 1
print(ans)
