#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWWOwecaFrIDFAV4(문제링크)
#1월 1일을 기준으로 m월 d일까지의 일수를 계산하여 요일 구하기
#day는 1월부터 12월까지의 일수를 저장한 리스트, hap은 1월 1일부터 현재 날짜까지의 일수
#res는 1월 1일(금)을 기준으로 계산하므로 금요일을 뜻하는 4부터 목요일을 뜻하는 3까지 저장한 리스트
#hap = day에서 주어진 월 전까지의 일수들의 합 + 주어진 일수 - 1
#현재 날짜에서 1월 1일을 뺀 일수를 계산해야 하므로 -1(-1을 하지 않는 경우, 요일이 하루씩 뒤로 밀림)
#hap을 7로 나눈 나머지값을 res의 인덱스로 대입하여 요일에 해당하는 숫자값 구하기
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
res = [4, 5, 6, 0, 1, 2, 3]
T = int(input())
for tc in range(1, T+1):
    m, d = map(int, input().split())
    hap = sum(day[:m]) + d - 1
    print(f'#{tc} {res[hap % 7]}')
