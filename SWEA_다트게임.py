#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXZuaLsqz9wDFAST(문제링크)
#주어진 공식을 이용하여 p = 11 - r / 20이라는 식 도출(p는 점수, r은 원의 반지름)
#math.sqrt(x*x + y*y)는 원점에서 화살이 꽂힌 지점까지의 거리
#위에서 구한 거리를 p = 11 - r / 20에서 r에 대입하여 화살에서 가장 가까운 원을 기준으로 점수 구하기
#화살이 꽂힌 지점을 '감싸는' 가장 가까운 원을 기준으로 점수를 구하므로 math.ceil을 이용하여 값 올림
#r / 20(=math.ceil(math.sqrt(x*x + y*y) / 20))이 0인 경우 즉, 반지름이 0인 경우는 10점
#r / 20이 11보다 큰 경우 가장 큰 원인 반지름이 200인 원보다 바깥에 있으므로 0점
#따라서 r / 20(d)이 11보다 작거나 같은 경우에만 점수 구해주기
#tc마다 print할 경우 시간초과가 발생하므로 정답을 res배열에 저장한 후 한꺼번에 출력하기
import sys
import math
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
res = []
for tc in range(1, T+1):
    n = int(input())
    score = 0
    for _ in range(n):
        x, y = map(int, input().split())
        d = math.ceil(math.sqrt(x*x + y*y) / 20)
        if d == 0:
            score += 10
        elif d <= 11:
            score += (11 - d)
    res.append(f'#{tc} {score}')
for r in res:
    print(r)
