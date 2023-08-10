import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1 ,0]
def DFS(x, y):
    global cnt
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0<=xx<=n-1 and 0<=yy<=n-1 and li[xx][yy] == 1:
            cnt += 1
            li[xx][yy] = 0
            DFS(xx, yy)

if __name__ == "__main__":
    n = int(input())
    li = [list(map(int, input().rstrip())) for _ in range(n)]
    ans = list()
    for i in range(n):
        for j in range(n):
            if li[i][j] == 1:
                cnt = 1
                li[i][j] = 0
                DFS(i, j)
                ans.append(cnt)
    print(len(ans))
    for a in sorted(ans):
        print(a)
