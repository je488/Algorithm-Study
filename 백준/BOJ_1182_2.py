import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
def go(i, sum):
    global ans
    if i == n:
        if sum == s:
            ans += 1
        return
    go(i+1, sum+a[i])
    go(i+1, sum)

go(0, 0)
if s == 0:
    ans -= 1
print(ans)