#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHz7xD6A20DFAVB(문제링크)
#n개의 정수가 공백 또는 줄바꿈으로 구분되어 있음
#따라서 s의 길이가 n이 될 때까지 문자열로 입력받고 replace() 함수를 이용하여 공백 제거
#res는 주어진 정수열(s)로 만들 수 없는 0 이상의 가장 작은 정수
#res를 0으로 초기화하고 문자로 바꾼 뒤 s에 포함되면 주어진 정수열로 만들 수 있으므로 s += 1
#res가 s에 포함되어 있지 않다면 만들 수 없는 정수이므로 정답
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
