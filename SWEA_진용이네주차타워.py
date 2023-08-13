import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    res = 0
    n, m = map(int, input().split())
    fee = [int(input()) for _ in range(n)]
    weight = [int(input()) for _ in range(m)]
    order = [int(input()) for _ in range(2*m)]
    order = deque(order)
    ch = [0] * n
    wait = deque()
    while order:
        tmp = order.popleft()
        if tmp > 0:
            if 0 not in ch:
                wait.append(tmp)
            else:
                idx = ch.index(0)
                ch[idx] = tmp
                res += fee[idx] * weight[tmp - 1]
        elif tmp < 0:
            idx = ch.index(abs(tmp))
            if wait:
                w = wait.popleft()
                ch[idx] = w
                res += fee[idx] * weight[w - 1]
            else:
                ch[idx] = 0
    print(f'#{tc} {res}')
