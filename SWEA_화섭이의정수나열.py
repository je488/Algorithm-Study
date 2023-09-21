import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    s = ''
    res = 0
    while len(s) != n:
        s += input().rstrip()
        s = s.replace(' ', '')
    while str(res) in s:
        res += 1
    print(f'#{tc} {res}')
