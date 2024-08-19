#인접 리스트를 이용하여 간선 저장
#정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문해야 하므로 a[i]를 오름차순으로 정렬
#그래프 탐색의 목적은 모든 정점을 한 번만 방문 -> 정점의 방문 여부를 확인하는 check 리스트 필요
#인접 리스트를 사용하였으므로 a[x]에는 x와 연결된 모든 정점이 저장되어 있음
#따라서 x와 연결된 정점(y)의 방문 여부만 체크하여 check[y]값이 0인 경우 정점(y) 방문
#DFS에서의 방문은 함수의 호출, BFS에서의 방문은 큐에 값을 넣을 때
#정점의 개수를 V, 간선의 개수를 E라고 할 때 인접 리스트를 이용하면 DFS, BFS 모두 O(V+E)
#인접 행렬을 이용하면 DFS, BFS 모두 O(V^2)이므로 인접 리스트를 사용하는 것이 좋음
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, start = map(int, input().split())
a = [[] for _ in range(n+1)]
check = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(1, n+1):
    a[i].sort()

def DFS(x):
    check[x] = 1
    print(x, end = ' ')
    for y in a[x]:
        if check[y] == 0:
            DFS(y)

def BFS(s):
    check = [0] * (n+1)
    Q = deque()
    Q.append(s)
    check[s] = 1
    while Q:
        x = Q.popleft()
        print(x, end = ' ')
        for y in a[x]:
            if check[y] == 0:
                check[y] = 1
                Q.append(y)

DFS(start)
print()
BFS(start)
print()
