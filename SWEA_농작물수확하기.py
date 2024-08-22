import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().rstrip())) for _ in range(n)]
    ans = 0
    s, e = n//2, n//2
    for i in range(n):
        for j in range(s, e+1):
            ans += a[i][j]
        if i < n//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f'#{tc} {ans}')