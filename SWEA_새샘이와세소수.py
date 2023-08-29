#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWaJ3q8qV-4DFAUQ(문제링크)
#n이 입력되면 에라토스테네스의 체를 이용하여 n보다 작은 소수 리스트 생성 -> primes
#3중 for문을 이용하여 소수 3개를 뽑아 더했을 때 합이 n과 같으면 res += 1
#소수 3개가 같은 값이어도 되고 순서를 따지지 않으므로 중복 조합
#따라서 i는 0부터, j는 i부터, k는 j부터 시작(i, j, k가 모두 0부터 시작하면 중복 순열)
#실행시간을 단축시키기 위해 정답을 ans배열에 저장한 후 한꺼번에 출력
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def makePrimes(n):
    primes = []
    ch = [0] * n
    for i in range(2, n):
        if ch[i] == 0:
            primes.append(i)
            for j in range(i, n, i):
                ch[j] = 1
    return primes
T = int(input())
ans = list()
for tc in range(1, T + 1):
    res = 0
    n = int(input())
    primes = makePrimes(n)
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] + primes[j] + primes[k] == n:
                    res += 1
    ans.append(f'#{tc} {res}')
for a in ans:
    print(a)

