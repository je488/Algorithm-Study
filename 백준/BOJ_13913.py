#BOJ_1697.py에 이동하는 방법을 추가로 출력하는 문제
#via[i]는 i가 어디에서 와서 최단 거리를 계산하였는지를 의미, via[i]에서 i로 이동
#now -> nxt이므로 via[nxt] = now
#n에서 k까지 이동 방법을 구하기 위해 via를 이용하여 k부터 n까지 이동 방법을 구하고 역순으로 출력
#go(n, k)는 n에서 k로 가는 방법을 출력하는 함수로 재귀를 이용하여 n부터 출력
#n은 시작점으로 이전 정점이 없기 때문에 n != k인 경우에만 출력
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 200000
sys.setrecursionlimit(MAX)
check = [0] * (MAX+1)
sec = [-1] * (MAX+1)
via = [-1] * (MAX+1)
n, k = map(int, input().split())
check[n] = 1
sec[n] = 0
Q = deque()
Q.append(n)
while Q:
    now = Q.popleft()
    for nxt in [now+1, now-1, now*2]:
        if 0 <= nxt < MAX and check[nxt] == 0:
            check[nxt] = 1
            sec[nxt] = sec[now] + 1
            via[nxt] = now
            Q.append(nxt)
print(sec[k])
def go(n, k):
    if n != k:
        go(n, via[k])
    print(k, end=' ')
go(n, k)
