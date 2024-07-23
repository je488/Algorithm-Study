import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    ans = 0
    a, b, c = map(int, input().split())
    if b >= c:
        ans += (b-c+1)
        b = c-1
    if a >= b:
        ans += (a-b+1)
        a = b-1
    if a < 1:
        ans = -1
    print(f'#{tc} {ans}')