import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    ans = -1
    for r in range(1, n+1):
        c = r
        while r * c <= n:
            tmp = a * abs(r - c) + b * (n - r * c)
            if ans == -1:
                ans = tmp
            else:
                ans = min(ans, tmp)
            c += 1
    print(f'#{tc} {ans}')