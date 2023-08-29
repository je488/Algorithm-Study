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
                if primes[i] + primes[j] + primes[k] == n:\
                    res += 1
    ans.append(f'#{tc} {res}')
for a in ans:
    print(a)

