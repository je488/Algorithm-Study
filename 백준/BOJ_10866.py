import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
dq = deque()
for _ in range(n):
    cmd, *val = input().split()
    if cmd == 'push_front':
        num = int(val[0])
        dq.appendleft(num)
    elif cmd == 'push_back':
        num = int(val[0])
        dq.append(num)
    elif cmd == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif cmd == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)