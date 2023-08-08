#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXO72aaqPrcDFAXS(문제링크)
#a부터 b까지 반복하며 제곱근(s)을 구하고 정수인지 확인
#제곱근이 정수면 i와 제곱근을 문자열로 변환하고 팰린드롬인지 확인
#i와 s가 모두 팰린드롬일 경우 i는 제곱 팰린드롬 수 이므로 cnt += 1
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
