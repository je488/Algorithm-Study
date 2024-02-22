import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
d = [0] * (k+1)
d[0] = 1
for i in range(n):
    for j in range(1, k+1):
        if j - coin[i] >= 0:
            d[j] += d[j - coin[i]]
print(d[k])