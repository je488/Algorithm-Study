import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    if n > a + b:
        minv = 0
    else:
        minv = (a + b) - n
    maxv = min(a, b)
    print(f'#{tc} {maxv} {minv}')
