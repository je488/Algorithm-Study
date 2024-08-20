import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    a = [[] for _ in range(n+1)]
    color = [0] * (n+1)
    for _ in range(m):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)

    def DFS(node, c):
        color[node] = c
        for next in a[node]:
            if color[next] == 0:
                if not DFS(next, 3-c):
                    return False
            elif color[next] == color[node]:
                return False
        return True

    ans = True
    for i in range(1, n+1):
        if color[i] == 0:
            if not DFS(i, 1):
                ans = False
    print('YES' if ans else 'NO')