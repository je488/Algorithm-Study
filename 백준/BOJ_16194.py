#BOJ_11052.py와 유사하나 카드 n개를 구매하는 비용의 최소값 구하기
#D[n] : 카드 n개를 구매하는 최소 비용
#D[i] = min(D[i-j] + P[j]) (1 <= j <= i)
#p[i] >= 1이므로 d[i] >= 1(d[0] = 0으로 예외) -> 정답은 항상 1 이상
#d를 0으로 초기화하면 결과가 항상 0이 되므로 올바른 정답을 구할 수 없음
#따라서 d를 -1로 초기화 -> d[i]가 -1이면 아직 정답을 구하지 않았음을 의미
#d[i]가 -1이면 바로 정답을 구하고 -1이 아니면 값을 비교하여 작은 경우에 정답 구하기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
p = [0] + list(map(int, input().split()))
d = [-1] * (n+1)
d[0] = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        if d[i] == -1 or d[i] > d[i-j] + p[j]:
            d[i] = d[i-j] + p[j]
print(d[n])
