import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
cnt = [0] * (n+1)
def go(idx, selected):
    if selected == m:
        for i in range(1, n+1):
            for j in range(1, cnt[i]+1):
                sys.stdout.write(str(i) + ' ')
        sys.stdout.write('\n')
        return
    if idx > n:
        return
    for i in range(m-selected, 0, -1):
        cnt[idx] = i
        go(idx+1, selected+i)
    cnt[idx] = 0
    go(idx+1, selected)

go(1, 0)