import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
a = [0] * 301
d = [0] * 301
for i in range(1, n+1):
    a[i] = int(input())
d[1] = a[1]
d[2] = d[1] + a[2]
for i in range(3, n+1):
    d[i] = max(d[i-2], d[i-3] + a[i-1]) + a[i]
print(d[n])