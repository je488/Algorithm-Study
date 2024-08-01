import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    t = n - m
    u = m - t
    print(f'#{tc} {u} {t}')