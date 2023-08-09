#li에서 최소값, 최대값의 좌표를 찾아 최소값의 좌표부터 상하좌우 4개의 가지로 뻗어나감
#x, y가 최대값의 좌표와 같아지면 도착이므로 res += 1
#dx, dy는 li에서 오른쪽, 아래, 왼쪽, 위를 탐색하기 위한 행과 열의 인덱스 증가치
#DFS를 호출하기 전에 좌표가 0과 n-1사이인지, 이동할 좌표의 값이 현재 좌표의 값보다 큰지 확인
#좌표 이동시, 값이 더 큰 좌표로만 이동이 가능하므로 이미 방문한 곳으로 되돌아갈 수 없음
#따라서 별도로 방문여부를 체크할 필요가 없음
#res += 1에서 res를 지역변수로 인식하여 에러 발생할 수 있음  -> global로 전역변수 표시
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def DFS(x, y):
    global res
    if x == ex and y == ey:
        res += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and li[x][y] < li[xx][yy]:
                DFS(xx, yy)

if __name__ == "__main__":
    res = 0
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    maxv, minv = -2147000000, 2147000000
    for i in range(n):
        for j in range(n):
            if li[i][j] > maxv:
                maxv = li[i][j]
                ex = i
                ey = j
            if li[i][j] < minv:
                minv = li[i][j]
                sx = i
                sy = j
    DFS(sx, sy)
    print(res)
