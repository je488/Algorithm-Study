#순간이동은 0초가 걸리고 걷기는 1초가 걸리므로 가중치는 0과 1
#따라서 큐를 2개로 분리 -> 현재 큐, 다음 큐
#현재 큐를 모두 방문하면 다음 큐가 현재 큐가 되고 새로운 비어있는 다음 큐 생성
#ex) 현재 큐가 0초이고 다음 큐가 1초인 경우
#ex) 0초 큐를 탐색할 때는 값을 0초 큐와 1초 큐에만 넣을 수 있음
#ex) 0초 큐를 모두 탐색한 경우 1초 큐가 현재 큐가 되고 2초 큐가 다음 큐가 됨
#ex) 1초 큐를 탐색할 때는 값을 1초 큐와 2초 큐에만 넣을 수 있음
#현재 큐와 다음 큐가 모두 비어있으면 반복문 종료
#check는 방문여부를 체크하기 위한 리스트로 값이 0이면 방문X, 1이면 방문
#dist는 몇 초만에 현재 위치(인덱스)를 방문했는지 저장하는 리스트
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 200000
check = [0] * MAX
dist = [-1] * MAX
n, m = map(int, input().split())
check[n] = 1
dist[n] = 0
Q = deque()
next_Q = deque()
Q.append(n)
while Q:
    now = Q.popleft()
    if now*2 < MAX and check[now*2] == 0:
        Q.append(now*2)
        check[now*2] = 1
        dist[now*2] = dist[now]
    if now-1 >= 0 and check[now-1] == 0:
        next_Q.append(now-1)
        check[now-1] = 1
        dist[now-1] = dist[now] + 1
    if now+1 < MAX and check[now+1] == 0:
        next_Q.append(now+1)
        check[now+1] = 1
        dist[now+1] = dist[now] + 1
    if not Q:
        Q = next_Q
        next_Q = deque()
print(dist[m])
