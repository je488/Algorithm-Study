import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def DFS(x, y):
    global res
    if x == 6 and y == 6:
        res += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and li[xx][yy] == 0:
                li[xx][yy] = 1
                DFS(xx, yy)
                li[xx][yy] = 0

if __name__ == "__main__":
    li = [list(map(int, input().split())) for _ in range(7)]
    res = 0
    li[0][0] = 1
    DFS(0, 0)
    print(res)
