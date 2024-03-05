#배열을 이용하여 큐 구현
#push, pop, size, empty, front, back 연산이 모두 시간 복잡도 O(1)이 되게 구현
#큐에는 begin ~ (end-1)까지 자료가 들어있음
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
Q = [0] * n
begin, end = 0, 0
for _ in range(n):
    cmd, *val = input().split()
    if cmd == 'push':
        num = int(val[0])
        Q[end] = num
        end += 1
    elif cmd == 'pop':
        if begin == end:
            print(-1)
        else:
            print(Q[begin])
            Q[begin] = 0
            begin += 1
    elif cmd == 'size':
        print(end - begin)
    elif cmd == 'empty':
        if begin == end:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if begin == end:
            print(-1)
        else:
            print(Q[begin])
    elif cmd == 'back':
        if begin == end:
            print(-1)
        else:
            print(Q[end-1])
