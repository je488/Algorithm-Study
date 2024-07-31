#큐 대신 덱(deque)을 사용 -> 큐와 달리 덱은 양쪽에서 값을 넣고 빼는 것이 가능
#순간이동은 덱의 앞에, 걷기는 덱의 뒤에 넣기
#BOJ_13549_1.py에서 현재 큐에 넣는 것을 덱의 앞에, 다음 큐에 넣은 것을 덱의 뒤에 넣기
#덱이 비어있으면 반복문 종료
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
Q.append(n)
while Q:
    now = Q.popleft()
    if now*2 < MAX and check[now*2] == 0:
        Q.appendleft(now*2)
        check[now*2] = 1
        dist[now*2] = dist[now]
    if now-1 >= 0 and check[now-1] == 0:
        Q.append(now-1)
        check[now-1] = 1
        dist[now-1] = dist[now] + 1
    if now+1 < MAX and check[now+1] == 0:
        Q.append(now+1)
        check[now+1] = 1
        dist[now+1] = dist[now] + 1
print(dist[m])
