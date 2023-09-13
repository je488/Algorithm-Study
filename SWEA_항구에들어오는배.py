import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    happy = list(int(input()) for _ in range(n))
    ships = set()
    res = 0
    for i in range(1, len(happy)):
        if happy[i] in ships:
            continue
        tmp = happy[i] - 1
        for j in range(tmp + 1, happy[-1] + 1, tmp):
            ships.add(j)
        res += 1
    print(f'#{tc} {res}')
