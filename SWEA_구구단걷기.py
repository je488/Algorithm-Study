#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYaf9W8afyMDFAQ9(문제링크)
#n이 36인 경우, 36이 적혀있는 셀은 (1,36),(2,18),(3,12),(4,9),(6,6),(9,4),(12,3),(18,2),(36,1)
#(6,6)을 기준으로 대칭되며 (4,9)와 (9,4)는 (1,1)로부터 이동거리가 11로 같음
#따라서 i가 1부터 6까지만 반복하면 모든 이동거리를 구할 수 있음
#n이 적혀있는 셀 중 (1,1)에서 이동거리가 최소인 셀은 (6,6) -> n의 제곱근
#제곱근에서 가까울수록 이동거리가 최소가 되므로 i가 n의 제곱근부터 1까지 1씩 감소하며 반복
#n의 제곱근은 정수가 아닐 수도 있으므로 int()이용
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    e = int(n**0.5)
    for i in range(e, 0, -1):
        if n % i == 0:
            res = (i-1) + (n//i - 1)
            break
    print('#{} {}'.format(tc, res))
