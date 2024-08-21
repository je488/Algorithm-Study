#인접 리스트를 이용하여 간선 저장
#check는 정점의 방문여부를 체크하는 리스트, cnt는 경로의 길이, ans는 최장 경로의 길이
#시작점에 따라 경로의 길이가 달라지므로 1 ~ n까지 모든 정점에서 시작해보기
#정점 x에 연결된 정점 중 방문하지 않은 정점이 있으면 check의 값을 1로 바꿔주고 방문
#더 이상 방문할 정점이 없으면 check 값을 다시 0으로 바꿔주기(다른 경로에서도 사용할 수 있도록)
#또한 현재 경로의 길이(cnt)가 지금까지 구한 최장 경로의 길이(ans)보다 크면 ans값 바꿔주기
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
