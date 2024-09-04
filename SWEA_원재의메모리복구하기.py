import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    memory = input().rstrip()
    cur = '0'
    ans = 0
    for m in memory:
        if m != cur:
            cur = m
            ans += 1
    print(f'#{tc} {ans}')