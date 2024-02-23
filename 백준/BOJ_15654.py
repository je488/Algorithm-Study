import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
check = [0] * n
ans = [0] * m
def go(idx):
    if idx == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(n):
        if check[i] == 1:
            continue
        check[i] = 1
        ans[idx] = a[i]
        go(idx+1)
        check[i] = 0

go(0)