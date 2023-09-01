#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXVyCaKugQDFAUo(문제링크)
#n이 주어지면 1부터 n까지 반복하며 n의 세제곱근이 되는 수 찾기
#반복문의 끝값을 n보다 작게 설정하면 n이 1일 때 반복문을 실행하지 않고 정답을 -1로 출력 -> 오답
#시간초과를 방지하기 위해 i*i*i가 n보다 커지면 break 후 -1 출력
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    res = -1
    for i in range(1, n+1):
        if i*i*i > n:
            break
        if i*i*i == n:
            res = i
            break
    print(f'#{tc} {res}')
