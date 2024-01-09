#에라토스테네스의 체를 이용하여 MAX값까지 모든 소수 구하기
#check는 0부터 MAX까지 소수인지 아닌지 판별하는 리스트, prime은 소수의 목록을 저장한 리스트
#check값이 False이면 소수이므로 prime 리스트에 추가
#A + B = N(N은 짝수, A와 B는 소수)임을 검증하기 위해 A가 소수일 때 B(N-A)도 소수인지 확인
#prime(미리 구한 모든 소수)의 값을 A라고 하여 N-A가 소수인지 check 리스트를 이용해 판별
#prime에서 2를 제외하는 이유는 N은 짝수이므로 A가 2가 되면 B도 짝수가 되어야 함
#하지만 B는 짝수가 될 수 없음(2가 유일한 짝수인 소수이므로) -> 따라서 A가 3인 경우부터 판별
#골드바흐의 추측은 10^18이하에서는 참인 것이 증명되어 있음
#따라서 주어진 MAX값의 범위에서는 A + B = N(N은 짝수, A와 B는 소수)이 되지 않는 경우는 없음
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 1000000
check = [0] * (MAX+1)
check[0] = check[1] = True
prime = []
for i in range(2, MAX+1):
    if check[i] == False:
        prime.append(i)
        j = i * i
        while j <= MAX:
            check[j] = True
            j += i
prime = prime[1:]
while True:
    n = int(input())
    if n == 0:
        break
    for p in prime:
        if check[n-p] == False:
            print("{0} = {1} + {2}".format(n, p, n-p))
            break
