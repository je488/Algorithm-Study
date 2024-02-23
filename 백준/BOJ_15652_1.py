import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = [0] * m
def go(idx, s):
    if idx == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(s, n+1):
        a[idx] = i
        go(idx+1, i)

go(0, 1)