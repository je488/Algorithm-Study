#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWpMsQfaCPMDFAQi(문제링크)
#반복문을 사용하여 문자열의 모든 문자를 반전시키는 경우 시간초과 발생 -> 규칙 찾기
#p3 = "001001100011011"
#p3에서 값이 "0"이 되는 인덱스는 0, 1, 3, 4, 7, 8, 9, 12
#p3에서 값이 "1"이 되는 인덱스는 2, 5, 6, 10, 11, 13, 12
#인덱스가 4의 배수인 경우 값이 0
#인덱스가 4의 배수가 아니면서 2의 배수인 경우 값이 1
#인덱스 i가 홀수인 경우, 짝수가 될 때까지 (i-1) // 2 반복 -> 짝수가 되면 위의 규칙 적용
#주어진 k가 1인 경우 첫번째 문자 즉, 0번 인덱스의 문자를 뜻하므로 k-1로 규칙 적용
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    k = int(input()) - 1
    while k % 2 == 1:
        k = (k - 1) // 2
    if k % 4 == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
