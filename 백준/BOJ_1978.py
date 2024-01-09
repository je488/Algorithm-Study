#어떤 수 N이 소수인지 아닌지 판별하기 위해 2 ~ √N까지 나누어 떨어지지 않는지 확인
#모든 수의 약수는 √N을 기준으로 대칭 -> √N보다 작은쪽에 약수가 없다면 √N보다 큰쪽에도 약수가 없음
#따라서 √N까지만 검사해줘도 소수인지 판별 가능 -> 시간복잡도 O(√N)
#컴퓨터에서 실수는 근사값을 나타내므로 i <= √N처럼 루트를 사용하기 보다는 i*i <= N과 같이 표현하기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

n = int(input())
a = list(map(int, input().split()))
ans = 0
for x in a:
    if is_prime(x):
        ans += 1
print(ans)
