#1. 간선 리스트를 이용하여 모든 간선에서 A -> B 간선 찾기
#2. 간선 리스트를 이용하여 모든 간선에서 C -> D 간선 찾기
#3. 인접 행렬을 이용하여 B -> C가 가능한지 확인
#4. 인접 리스트를 이용하여 D에서 갈 수 있는 정점 중 A, B, C, D가 아닌 것이 있는지 확인
#a는 인접 행렬, g는 인접 리스트, edges는 간선 리스트
#친구 관계는 양방향이므로 a, g, edges에 u -> v, v -> u 각각 저장하기
#m은 간선의 개수로 양방향이므로 *2
#2중 for문을 이용하여 A -> B C -> D인지, A B C D가 모두 다른지 확인
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
a = [[False] * n for _ in range(n)]
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    edges.append((v, u))
    a[u][v] = a[v][u] = True
    g[u].append(v)
    g[v].append(u)
m *= 2
for i in range(m):
    for j in range(m):
        A, B = edges[i]
        C, D = edges[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not a[B][C]:
            continue
        for E in g[D]:
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            sys.exit(0)
print(0)
