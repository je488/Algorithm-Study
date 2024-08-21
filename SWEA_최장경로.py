import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(x, cnt):
    global ans
    check[x] = 1
    for y in a[x]:
        if check[y] == 0:
            DFS(y, cnt + 1)
    check[x] = 0
    if ans < cnt:
        ans = cnt

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    a = [[] for _ in range(n + 1)]
    check = [0] * (n + 1)
    ans = 0
    for _ in range(m):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)

    for i in range(1, n + 1):
        DFS(i, 1)
    print(f'#{tc} {ans}')