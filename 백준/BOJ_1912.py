import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
d = [0] * n
for i in range(n):
    d[i] = a[i]
    if i == 0:
        continue
    if d[i] < d[i-1] + a[i]:
        d[i] = d[i-1] + a[i]
print(max(d))