#테스트케이스마다 g(N)을 구하면 시간초과 발생 -> N의 최댓값까지 모든 g(N)을 미리 구하고 활용
#d[i] = i의 모든 약수의 합, s[i] = d[1] + ... + d[i]
#첫번째 반복문에서 i를 약수로 갖는 모든 수(i의 배수 = i*j)에 i값 누적 -> 모든 d(N) 구하기
#1은 모든 수의 약수이므로 d를 모두 1로 초기화하고 반복문도 2부터 시작
#반복문의 횟수는 n/2 + n/3 + ... + n/n = n(1/2 + 1/3 + ... + 1/n) <= nlgn(시간복잡도)
#두번째 반복문에서 구해놓은 d의 값을 이용하여 s값 누적 -> 모든 s(N)값 구하기 -> 시간복잡도 N
#세번째 반복문에서 테스트케이스마다 n을 입력받고 정답을 ans에 저장하므로 시간복잡도 T
#총 시간복잡도 = NlgN + N + T = NlgN + T
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 1000000
d = [1] * (MAX+1)
s = [0] * (MAX+1)
for i in range(2, MAX+1):
    j = 1
    while i * j <= MAX:
        d[i*j] += i
        j += 1
for i in range(1, MAX+1):
    s[i] = s[i-1] + d[i]
T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    ans.append(s[n])
print('\n'.join(map(str, ans)) + '\n')
