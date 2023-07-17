#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYcllbDqUVgDFASR(문제링크)
#1사분면을 기준으로 격자점의 개수를 구한 뒤 * 4(단, (0,1),(2,0)과 같이 좌표축에 위치하거나 원점인 경우 제외)
#(1,0)(-1,0)(0,1)(0,-1)과 같이 좌표축 위에 위치한 격자점의 개수는 n * 4
#(0,0)도 원 안에 포함되므로 +1
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    for x in range(1, n):
        for y in range(1, n):
            if x*x + y*y <= n*n:
                cnt += 1
    print('#{} {}'.format(tc, cnt*4 + n*4 + 1))
