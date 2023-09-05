#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWRuoqCKkE0DFAXt(문제링크)
#테스트케이스별로 소수를 찾으면 시간초과가 발생하므로 미리 소수를 판별하는 리스트(ch) 생성
#에라토스테네스의 체를 이용하여 1부터 a와 b의 최댓값인 1000000까지 소수인지 아닌지 ch에 체크
#ch는 인덱스가 소수인 경우 값이 0, 소수가 아닌 경우 값이 1인 리스트
#a부터 b까지 k로 반복하며 소수인지 체크하고 소수이면 k를 문자열로 바꿔서 d가 포함되는지 체크
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = 1000000
ch = [0] * (N+1)
ch[1] = 1
for i in range(2, int(N**0.5)+1):
    for j in range(i*i, N+1, i):
        ch[j] = 1
T = int(input())
for tc in range(1, T + 1):
    d, a, b = map(int, input().split())
    d = str(d)
    res = 0
    for k in range(a, b+1):
        if ch[k] == 0:
            if d in str(k):
                res += 1
    print(f'#{tc} {res}')
