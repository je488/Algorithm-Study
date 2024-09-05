import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
password = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
def find_code(a):
    for i in range(n):
        for j in range(m-1, -1, -1):
            if a[i][j] == '1':
                code = a[i][j-55:j+1]
                return code
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = [input().rstrip() for _ in range(n)]
    code = find_code(a)
    num = []
    for i in range(0, 56, 7):
        num.append(password[code[i:i+7]])
    if (sum(num[0::2]) * 3 + sum(num[1::2])) % 10 == 0:
        ans = sum(num)
    else:
        ans = 0
    print(f'#{tc} {ans}')