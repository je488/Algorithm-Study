import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    dn = list(input().split())
    dm = list(input().split())
    cnt = n + m
    set_cnt = len(set(dn + dm))
    ans = cnt - set_cnt
    print(f'#{tc} {ans}')