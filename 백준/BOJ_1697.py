#동생을 찾는 가장 빠른 시간 즉, 최소 시간을 구하는 문제로 BFS 이용
#BFS의 시간 복잡도는 O(V+E)
#1 <= N, K <= 10만이므로 정점의 개수(V)는 10만
#하나의 정점마다 3가지 방법으로 이동이 가능하므로 간선의 개수(E)는 10만*3 = 30만
#따라서 시간 복잡도는 약 40만으로 BFS로 해결 가능
#check는 방문여부를 체크하는 리스트(방문했으면 True, 방문하지 않았으면 False)
#sec는 몇 초만에 현재 위치(인덱스)를 방문했는지 저장하는 리스트
#큐에 수빈이의 위치를 넣어가면서 이동
#다음에 이동할 위치(nxt)가 범위를 넘어가지 않고 이전에 방문하지 않았으면 다음 위치로 이동
#다음 위치로 이동하면 check 리스트와 sec 리스트의 값을 바꿔주고 큐에 다음 위치 넣기
#시작점에서 다음 위치로 가기까지 걸리는 시간은 시작점에서 현재 위치까지 오는 데 걸린 시간 + 1
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 100000
check = [0] * (MAX+1)
sec = [-1] * (MAX+1)
n, k = map(int, input().split())
Q = deque()
Q.append(n)
check[n] = 1
sec[n] = 0
while Q:
    now = Q.popleft()
    for nxt in [now+1, now-1, now*2]:
        if 0 <= nxt <= MAX and check[nxt] == 0:
            check[nxt] = 1
            sec[nxt] = sec[now] + 1
            Q.append(nxt)
print(sec[k])
