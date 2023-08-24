import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def DFS(x, y, h):
    ch[x][y] = 1
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        if 0<=xx<n and 0<=yy<n and li[xx][yy] > h and ch[xx][yy] == 0:
            DFS(xx, yy, h)

if __name__ == "__main__":
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    maxv = -2147000000
    res = 0
    for i in li:
        if maxv < max(i):
            maxv = max(i)
    for rain in range(maxv):
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for j in range(n):
            for k in range(n):
                if li[j][k] > rain and ch[j][k] == 0:
                    cnt += 1
                    DFS(j, k, rain)
        if res < cnt:
            res = cnt
    print(res)
