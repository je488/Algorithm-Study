import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = [0] * m
def go(idx, s):
    if idx == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(s, n):
        ans[idx] = a[i]
        go(idx+1, i)

go(0, 0)