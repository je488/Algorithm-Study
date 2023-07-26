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
