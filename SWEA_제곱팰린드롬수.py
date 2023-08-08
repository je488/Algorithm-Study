import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b+1):
        s = i ** 0.5
        if s == int(s):
            i = str(i)
            s = str(int(s))
            if i == i[::-1] and s == s[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')
