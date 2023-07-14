import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(v):
    global res
    if v == n:
        res += 1
        print(*path)
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                ch[i] = 0
                path.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    res = 0
    path = []
    for _ in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    ch[1] = 1
    path.append(1)
    DFS(1)
    print(res)
