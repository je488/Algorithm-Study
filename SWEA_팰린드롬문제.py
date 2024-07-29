import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    yPal = []
    nPal = []
    for _ in range(n):
        s = input().rstrip()
        if s == s[::-1]:
            yPal.append(s)
        else:
            nPal.append(s)
    ans = 0
    if len(yPal) >= 1:
        ans += m
    for i in nPal:
        if i[::-1] in nPal:
            ans += m
    print(f'#{tc} {ans}')