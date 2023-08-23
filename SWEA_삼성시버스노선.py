import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    cnt = [0] * 5001
    res = list()
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            cnt[i] += 1
    p = int(input())
    for _ in range(p):
        c = int(input())
        res.append(cnt[c])
    print(f'#{tc}', *res)
