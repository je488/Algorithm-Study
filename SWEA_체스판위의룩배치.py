import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    res = 'yes'
    li = [list(input().rstrip()) for _ in range(8)]
    cli = [list(x) for x in (zip(*li))]
    for i in range(8):
        if li[i].count('O') != 1 or cli[i].count('O') != 1:
            res = 'no'
            break
    print(f'#{tc} {res}')
