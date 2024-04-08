import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(1, (1 << n)):
    sum = 0
    for k in range(n):
        if i & (1 << k):
            sum += a[k]
    if sum == s:
        ans += 1
print(ans)