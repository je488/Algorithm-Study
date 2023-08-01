import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
s, e = map(int, input().split())
dQ = deque()
dQ.append(s)
dis[s] = 0
ch[s] = 1
while dQ:
    now = dQ.popleft()
    if now == e:
        break
    for next in (now-1, now+1, now+5):
        if 0<next<=MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
print(dis[e])
