import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    for x in range(1, n):
        for y in range(1, n):
            if x*x + y*y <= n*n:
                cnt += 1
    print('#{} {}'.format(tc, cnt*4 + n*4 + 1))
