import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = [0] * m
def go(idx, cnt):
    if cnt == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    if idx > n:
        return
    a[cnt] = idx
    go(idx+1, cnt+1)
    a[cnt] = 0
    go(idx+1, cnt)

go(1, 0)