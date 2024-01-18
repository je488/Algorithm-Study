import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
t = [0] * n
p = [0] * n
for i in range(n):
    t[i], p[i] = map(int, input().split())
ans = 0
def go(day, s):
    global ans
    if day == n:
        ans = max(ans, s)
        return
    if day > n:
        return
    go(day + t[day], s + p[day])
    go(day + 1, s)

go(0, 0)
print(ans)