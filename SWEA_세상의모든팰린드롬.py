import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    s = list(input().rstrip())
    if s == s[::-1]:
        res = 'Exist'
    else:
        for i in range(len(s)):
            if s[i] == '?':
                s[i] = s[-i - 1]
        if s == s[::-1]:
            res = 'Exist'
        else:
            res = 'Not exist'
    print(f'#{tc} {res}')
