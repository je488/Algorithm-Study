import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    s = input().rstrip()
    res = 'Exist'
    for i in range(len(s)//2):
        if s[i] == '*' or s[-1-i] == '*':
            break
        if s[i] != s[-1-i]:
            res = 'Not exist'
            break
    print(f'#{tc} {res}')



