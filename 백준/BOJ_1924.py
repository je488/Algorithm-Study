#date는 1월부터 12월까지의 일수를 저장한 리스트
#week는 정답을 출력하기 위해 요일을 저장한 리스트
#res는 2006년 12월 31일부터 x월 y일까지 며칠이 지났는지 저장하는 변수
#x, y가 3, 14인 경우 date[0]과 date[1] 즉, 1월과 2월의 일수와 14(y값)를 res에 더하기
#x, y가 1, 1인 경우 date값은 더하지 않고 y값 즉, 1만 더하여 res = 1
#res를 7로 나눈 나머지를 구하고 week에서 값을 찾아 출력하기
#다른 방법으로는 calendar 모듈의 weekday 함수를 이용하여 요일 정보를 얻을 수 있음
#ex) day = calendar.weekday(2007, x, y)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
x, y = map(int, input().split())
res = 0
for i in range(x-1):
    res += date[i]
res += y
print(week[res % 7])
