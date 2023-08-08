#(0, 0)부터 상하좌우 4개의 가지로 뻗어나감 -> (6, 6)이 되면 도착이므로 res += 1
#dx, dy는 li에서 오른쪽, 아래, 왼쪽, 위를 탐색하기 위한 행과 열의 인덱스 증가치
#ch를 따로 생성하지 않고 li의 값으로 방문여부 표시(방문하면 값을 1(벽)로 바꿔주기)
#DFS를 호출하기 전에 좌표가 0과 6사이인지 확인하고 방문한 적이 없는지(벽이 아닌지) 체크
#DFS에서 다시 back했을 때(되돌아왔을 때) li의 값을 0으로 바꿔 다시 방문할 수 있게 함
#res += 1에서 res를 지역변수로 인식하여 에러 발생할 수 있음 -> global로 전역변수 표시
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
