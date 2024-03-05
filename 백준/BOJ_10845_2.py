#collections.deque를 이용하여 큐 구현
#input = sys.stdin.readline 없으면 시간초과
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
Q = deque()
for _ in range(n):
    cmd, *val = input().split()
    if cmd == 'push':
        num = int(val[0])
        Q.append(num)
    elif cmd == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(Q))
    elif cmd == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif cmd == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)
