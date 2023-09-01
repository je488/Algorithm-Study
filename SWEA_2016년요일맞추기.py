import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
res = [4, 5, 6, 0, 1, 2, 3]
T = int(input())
for tc in range(1, T+1):
    m, d = map(int, input().split())
    hap = sum(day[:m]) + d - 1
    print(f'#{tc} {res[hap % 7]}')
