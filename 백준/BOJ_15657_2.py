import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = [0] * n
def go(idx, selected):
    if selected == m:
        for i in range(n):
            for j in range(cnt[i]):
                sys.stdout.write(str(a[i]) + ' ')
        sys.stdout.write('\n')
        return
    if idx >= n:
        return
    for i in range(m-selected, 0, -1):
        cnt[idx] = i
        go(idx+1, selected+i)
    cnt[idx] = 0
    go(idx+1, selected)

go(0, 0)