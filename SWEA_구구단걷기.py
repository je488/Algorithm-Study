import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    e = int(n**0.5)
    for i in range(e, 0, -1):
        if n % i == 0:
            res = (i-1) + (n//i - 1)
            break
    print('#{} {}'.format(tc, res))
