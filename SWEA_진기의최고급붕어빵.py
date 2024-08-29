import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 'Possible'
    for i in range(n):
        bread = (a[i] // m) * k
        if bread < i+1:
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')