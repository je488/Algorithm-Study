#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXMCXV_qVgkDFAWv(문제링크)
#A와 B의 교집합의 최대, 최소를 구하는 문제
#최대값은 a와 b중 더 작은 값이 되고 최소값은 n(A ∪ B) = n(A) + n(B) - n(A ∩ B) 이용
#a와 b를 합한 값이 n보다 작은 경우는 최소값이 위의 식을 적용했을 때 음수가 됨
#따라서 if문을 이용하여 a와 b를 합한 값이 n보다 작은 경우 최소값은 0
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    if n > a + b:
        minv = 0
    else:
        minv = (a + b) - n
    maxv = min(a, b)
    print(f'#{tc} {maxv} {minv}')
