#li에서 값이 1인 좌표를 찾고 상하좌우 4개의 가지로 뻗어나감
#dx, dy는 li에서 오른쪽, 아래, 왼쪽, 위를 탐색하기 위한 행과 열의 인덱스 증가치
#cnt는 단지별 집의 개수로 li의 행과 열을 탐색하면서 집을 발견하면 1로 초기화
#이미 방문한 곳은 다시 방문하지 않기 위해 li의 값을 0으로 변경
#DFS를 호출하기 전에 좌표가 0과 n-1사이인지, li의 값이 1(집)인지 확인
#DFS에서 back했을 때 단지별 집의 개수를 ans에 추가하고 오름차순으로 출력
#단지 하나를 모두 탐색했을 때 ans에 추가하므로 총 단지수는 ans의 길이와 같음
#cnt += 1에서 cnt를 지역변수로 인식하여 에러 발생할 수 있음 -> global로 전역변수 표시
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
