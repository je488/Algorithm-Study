#Bottom-up 방식 이용(Top-down 방식을 이용하는 경우 메모리 초과 발생)
#D[N] : N을 1로 만드는 최소 연산 횟수
#N이 3으로 나누어 떨어지는 경우 N -> N/3 -> ... -> 1이므로 D[N] = D[N/3] + 1
#N이 2로 나누어 떨어지는 경우 N -> N/2 -> ... -> 1이므로 D[N] = D[N/2] + 1
#N에서 1을 빼는 경우 N -> N-1 -> ... -> 1이므로 D[N] = D[N-1] + 1
#D[N] = min(D[N/3], D[N/2], D[N-1]) + 1
#가장 작은 크기의 문제는 D[1]로 1을 1로 만들기 위해서는 연산이 필요없으므로 D[1] = 0
#D[N/3]과 D[N/2]는 각각 3과 2로 나누어 떨어질 때만 사용이 가능
#따라서 D[N-1]을 이용하여 D[N]의 값을 구한 뒤 3이나 2로 나누어 떨어지면 비교하여 최소값 구하기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
d = [0] * (n + 1)
d[1] = 0
for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1
    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1
print(d[n])
