import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = [0] * m
def go(idx, cnt):
    if cnt == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    if idx >= n:
        return
    ans[cnt] = a[idx]
    go(idx+1, cnt+1)
    ans[cnt] = 0
    go(idx+1, cnt)

go(0, 0)