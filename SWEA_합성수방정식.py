#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYYAGCNKPgIDFARc(문제링크)
#iscn함수를 이용하여 합성수인지 판별(2부터 s의 제곱근까지 반복하고 하나라도 나누어 떨어지면 True 리턴)
#무한반복하다가 i와 i+n이 모두 합성수이면 출력 후 반복문 탈출
#1부터 3까지는 합성수가 아니므로 i는 4부터 시작
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def iscn(s):
    for i in range(2, int(s**0.5)+1):
        if s % i == 0:
            return True
    return False
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    i = 4
    while True:
        if iscn(i) and iscn(i + n):
            print(f'#{tc} {i+n} {i}')
            break
        i += 1
