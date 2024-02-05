#D[n] : 카드 n개를 구매하는 최대 비용
#맨 마지막에 구매할 수 있는 카드팩은 1번째 카드팩 ~ N번째 카드팩 중 하나
#맨 마지막에 1번째 카드팩을 구매한 경우 : D[n-1] + P[1]
#맨 마지막에 2번째 카드팩을 구매한 경우 : D[n-2] + P[2]
#맨 마지막에 n번째 카드팩을 구매한 경우 : D[0] + P[n]
#D[i] = max(D[i-j] + P[j]) (1 <= j <= i)
#D[0]은 카드 0개를 구매하는 최대 비용이므로 카드팩을 구매하지 않음 -> D[0] = 1
#카드를 구매하는 비용은 음수가 될 수 없으므로 d[i] >= 0 -> d를 0으로 초기화
#시간 복잡도 : N(전체 문제의 개수) * N(문제 1개를 푸는 시간, 점화식의 시간 복잡도) -> O(N^2)
#i의 최대값은 N이므로 j도 1 ~ N까지 탐색 가능 -> 문제 1개를 푸는 시간 N
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
p = [0] + list(map(int, input().split()))
d = [0] * (n+1)
for i in range(1, n+1):
    for j in range(1, i+1):
        d[i] = max(d[i], d[i-j] + p[j])
print(d[n])
