#find_code(a)는 a에서 56자리 암호코드 정보를 찾아 리턴하는 함수
#암호코드가 여러 줄이라도 내용은 같으므로 한 줄만 찾아서 리턴
#암호코드에서 숫자 하나는 7개의 비트로 암호화되어 있으므로 code를 7개씩 슬라이싱
#슬라이싱한 7자리 코드를 password에서 찾아 숫자로 변환하여 num 리스트에 저장
#num을 바탕으로 올바른 암호코드인지 판별하여 올바른 암호코드이면 num의 합, 올바르지 않으면 0
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
