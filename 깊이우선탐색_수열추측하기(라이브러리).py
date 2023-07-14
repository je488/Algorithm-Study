#DFS대신 itertools 라이브러리 이용
#a리스트에 1부터 n까지 값을 넣고 permutations() 이용하여 순열 구하기(조합은 combinations())
#구한 순열에서 각각의 경우의 수에 b(미리 구해놓은 이항계수)를 곱하고 더해서 sum구하기
#enumerate를 이용하여 x(숫자 하나)와 b[L](숫자에 곱할 이항계수 값)을 곱해서 sum에 누적
#sum이 f값과 같으면 출력하고 break(사전 순으로 가장 앞에 오는 것만 출력)
import sys
import itertools as it
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, f = map(int, input().split())
b = [1] * n
for i in range(1, n):
    b[i] = b[i-1] * (n-i) // i
a = list(range(1, n+1))
for tmp in it.permutations(a):
    sum = 0
    for L, x in enumerate(tmp):
        sum += (x * b[L])
    if sum == f:
        print(*tmp)
        break
