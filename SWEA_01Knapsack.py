import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        v, c = map(int, input().split())
        for j in range(1, k+1):
            if v <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-v] + c)
            else:
                dp[i][j] = dp[i-1][j]
    print(f'#{tc} {dp[n][k]}')