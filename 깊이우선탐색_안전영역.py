#너비우선탐색_안전영역과 같은 문제
#주어진 높이 정보에서 최댓값을 찾아 비의 양이 0부터 최댓값-1일 때 각각 안전영역의 개수 세기
#비의 양이 최댓값이면 모두 잠겨 안전영역의 개수가 0이므로 최댓값-1까지만 반복
#안전영역의 개수를 세기 위해 li에서 값이 비의 양보다 크고 이전에 방문한 적이 없는 좌표 찾기
#찾은 좌표를 기준으로 상하좌우 탐색 -> 4개의 가지로 뻗어나감
#좌표를 찾으면 안전영역 한 개를 찾은 것과 같으므로 cnt(안전영역의 수) += 1
#dx, dy는 li에서 오른쪽, 아래, 왼쪽, 위를 탐색하기 위한 행과 열의 인덱스 증가치
#ch는 중복 방문하지 않기 위해 방문여부를 체크하는 리스트 -> 비의 양이 바뀔 때마다 초기화
#DFS를 호출하기 전에 좌표가 경계선을 넘지 않고 방문한 적이 없고 li의 값이 비의 양보다 큰지 확인
#안전영역의 개수가 이전에 구한 안전영역의 최대 개수(res)보다 크면 res값을 cnt로 바꿔주기
#sys.setrecursionlimit(10**6)는 재귀의 최대 깊이를 10**6으로 설정
#파이썬에서 기본으로 설정된 재귀 깊이는 1000 / 위 코드를 작성하지 않으면 Recursion Error 발생
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
