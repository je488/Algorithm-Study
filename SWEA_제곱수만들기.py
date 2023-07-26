#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXH_h695kDFAST(문제링크)
#주어진 자연수 a의 소인수들을 구해서 각 지수가 홀수인 소인수를 곱해서 제곱수 만들기
#ex) 60 = 2^2 * 3 * 5 -> 3과 5가 지수가 1로 홀수이므로 3*5=15를 곱해주기
#입력된 a마다 반복해서 소인수를 구하는 것은 비효율적이므로 미리 소수 리스트(primes) 만들기
#a를 소수의 제곱으로 나누고 나누어 떨어지면 a의 값을 소수의 제곱으로 나눈 몫으로 바꾸기
#지수가 짝수인 소인수들을 나눠서 없애줌 -> 지수가 홀수인 소인수들만 남음 -> 정답
#tc마다 print할 경우 시간초과가 발생하므로 정답을 res배열에 저장한 후 한꺼번에 출력하기

#에라토스테네스의 체를 이용하여 a의 최댓값인 10000000의 제곱근 + 1까지 소수 리스트 생성
#소수 리스트를 10000000의 제곱근(3162)까지만 구하면 primes의 마지막 값은 3137
#ex) a가 9998245일 경우, 9998245 = 5 * 1249 * 1601로 반복문에서 if문에 한번도 걸리지 않음
#따라서 a가 그대로 정답이 되어야 하나 primes의 마지막값인 3137의 제곱보다 커서 i += 1
#i가 primes의 마지막 인덱스보다 커지므로 list index out of range 에러 발생
#따라서 10000000의 제곱근인 3162에 1을 더한 3163까지 소수 리스트 만들기
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
primes = []
ch = [0] * (int(10000000 ** 0.5) + 2)
for i in range(2, int(10000000 ** 0.5) + 2):
    if ch[i] == 0:
        primes.append(i)
        for j in range(i, int(10000000 ** 0.5) + 2, i):
            ch[j] = 1
T = int(input())
res = []
for tc in range(1, T+1):
    a = int(input())
    i = 0
    while a >= primes[i] * primes[i]:
        if a % (primes[i]*primes[i]) == 0:
            a = a // (primes[i]*primes[i])
        else:
            i += 1
    res.append(f'#{tc} {a}')
for r in res:
    print(r)
