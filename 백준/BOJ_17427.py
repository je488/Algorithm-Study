#1부터 N까지 약수를 모두 구해서 더하는 것은 시간복잡도가 O(N²) 또는 O(N√N)이므로 시간초과 발생
#따라서 "약수의 반대는 배수"인 것을 이용하여 문제 풀기
#N이하의 자연수에서 1을 약수로 갖는 수의 개수 = N이하의 자연수에서 1의 배수의 개수 = N // 1
#N이하의 자연수에서 1이 약수로 총 N // 1개 있으므로 1의 총합은 (N // 1) * 1
#g(N) = (N // 1) * 1 + (N // 2) * 2 + (N // 3) * 3 + ... + (N // N) * N
#위의 식을 이용하면 시간복잡도는 각각 나누고 곱하는 데 O(1), 총 N번 더하므로 O(N)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
res = 0
for i in range(1, n+1):
    res += (n // i) * i
print(res)
