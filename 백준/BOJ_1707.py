#인접 리스트를 이용하여 간선 저장
#color는 방문 여부를 확인하고 그래프를 구분하기 위한 리스트(그래프를 A 또는 B로 구분)
#color 값이 0이면 방문X, 1이면 A, 2이면 B
#DFS의 리턴값이 True인 경우 이분 그래프, False인 경우 이분 그래프X
#DFS(node, c)는 node에 방문하고 node의 색상은 c(1 또는 2)임을 의미
#node를 이미 방문한 경우 색상만 비교, 색상이 같으면 이분 그래프가 아니므로 False 리턴
#node -> next에서 node의 색상이 c이면 next의 색상은 3-c
#중간에 하나라도 리턴값이 False이면 이분 그래프X
#이분 그래프는 연결 요소가 1보다 커도 상관 없으므로 1부터 n까지 모두 검사
#input = sys.stdin.readline 없으면 시간 초과
#sys.setrecursionlimit(1000000) 없으면 Recursion Error 발생
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
