import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
a = [0] + [int(input()) for _ in range(n)]
d = [0] * (n+1)
d[1] = a[1]
if n >= 2:
    d[2] = a[1] + a[2]
for i in range(3, n+1):
    d[i] = d[i-1]
    d[i] = max(d[i], d[i-2] + a[i])
    d[i] = max(d[i], d[i-3] + a[i-1] + a[i])
print(d[n])