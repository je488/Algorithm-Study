import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    D, L, N = map(int, input().split())
    i = 0
    sum = 0
    for i in range(N):
        sum += D*(1+(i*L*0.01))
    print(f'#{tc} {int(sum)}')
