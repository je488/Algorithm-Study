import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cards = list(input().split())
    res = list()
    l = 0
    r = (n+1) // 2
    for _ in range(n//2):
        res.append(cards[l])
        res.append(cards[r])
        l += 1
        r += 1
    if n % 2 == 1:
        res.append(cards[n//2])
    print(f'#{tc}', *res)
