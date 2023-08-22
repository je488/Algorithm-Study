import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    k = int(input()) - 1
    while k % 2 == 1:
        k = (k - 1) // 2
    if k % 4 == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
