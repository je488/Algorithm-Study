import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
for tc in range(1, T + 1):
    res = 0
    s = input().rstrip()
    for i in range(len(s)):
        if s[i] == alpha[i]:
            res += 1
        else:
            break
    print(f'#{tc} {res}')
