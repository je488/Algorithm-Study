import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def extended_euclid(a, b):
    x1 = 1
    y1 = 0
    r1 = a
    x2 = 0
    y2 = 1
    r2 = b
    while r2 != 0:
        q = r1 // r2
        rt = r1 - q * r2
        xt = x1 - q * x2
        yt = y1 - q * y2

        x1, y1, r1 = x2, y2, r2
        x2, y2, r2 = xt, yt, rt
    if r1 != 1:
        return 0
    return x1

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    x = extended_euclid(a, b)
    if x == 0:
        print(f'#{tc} -1')
    else:
        y = (1 - a * x) // b
        print(f'#{tc} {x} {y}')