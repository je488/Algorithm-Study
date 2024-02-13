import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
d = [[0] * 10 for _ in range(1001)]
mod = 10007
for i in range(10):
    d[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1):
            d[i][j] += d[i-1][k]
            d[i][j] %= mod
ans = sum(d[n])
print(ans % mod)