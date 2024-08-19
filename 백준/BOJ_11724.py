#인접 리스트를 이용하여 간선 저장
#check는 정점의 방문여부를 체크하는 리스트로 check값이 True면 방문, False면 방문X
#DFS나 BFS 탐색을 이용하여 연결 요소의 개수를 구할 수 있음(코드에서는 DFS 이용)
#DFS, BFS 모두 한 정점에서 연결된 모든 정점을 방문하는 알고리즘
#따라서 DFS나 BFS의 시작은 연결 요소 1개를 찾은 것과 같음
#1부터 n까지 탐색하면서 방문하지 않은 정점일 때 DFS 시작(연결 요소의 개수 1 증가)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
check = [False] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

def DFS(x):
    check[x] = True
    for y in a[x]:
        if check[y] == False:
            DFS(y)

ans = 0
for i in range(1, n+1):
    if not check[i]:
        DFS(i)
        ans += 1
print(ans)
