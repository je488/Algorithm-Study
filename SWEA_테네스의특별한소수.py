import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = 1000000
ch = [0] * (N+1)
ch[1] = 1
for i in range(2, int(N**0.5)+1):
    for j in range(i*i, N+1, i):
        ch[j] = 1
T = int(input())
for tc in range(1, T + 1):
    d, a, b = map(int, input().split())
    d = str(d)
    res = 0
    for k in range(a, b+1):
        if ch[k] == 0:
            if d in str(k):
                res += 1
    print(f'#{tc} {res}')
