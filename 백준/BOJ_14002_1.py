import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
d = [0] * n
v = [-1] * n
for i in range(n):
    d[i] = 1
    for j in range(0, i):
        if a[j] < a[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            v[i] = j
ans = max(d)
p = [i for i, x in enumerate(d) if x == ans][0]
print(ans)
s = []
while p != -1:
    s.append(p)
    p = v[p]
s = s[::-1]
for i in s:
    print(a[i], end = ' ')