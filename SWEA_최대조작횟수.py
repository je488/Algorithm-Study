import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    sub = b - a
    if sub == 0:
        ans = 0
    elif sub <= 1:
        ans = -1
    else:
        if sub % 2 == 0:
            ans = sub // 2
        else:
            ans = (sub - 3) // 2 + 1
    print(f'#{tc} {ans}')