import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    res = -1
    for i in range(n+1):
        if i*i*i > n:
            break
        if i*i*i == n:
            res = i
            break
    print(f'#{tc} {res}')
