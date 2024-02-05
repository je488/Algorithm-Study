#D[n] : n을 1, 2, 3의 합으로 나타내는 방법의 수
#정수 n을 1, 2, 3의 합으로 나타낼 때 가장 마지막에 더할 수 있는 수는 1, 2, 3
#가장 마지막에 1을 더하는 경우 앞에서 n-1을 만들고 +1 -> D[n-1]
#가장 마지막에 2을 더하는 경우 앞에서 n-2을 만들고 +2 -> D[n-2]
#가장 마지막에 3을 더하는 경우 앞에서 n-3을 만들고 +3 -> D[n-3]
#D[n] = D[n-1] + D[n-2] + D[n-3]
#1 <= N <= 10이므로 모든 d[N]의 값을 미리 구해놓기
#수를 0개 사용하는 것도 가능하므로 d[0] = 1
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
d = [0] * 11
d[0] = 1
for i in range(1, 11):
    if i - 1 >= 0:
        d[i] += d[i - 1]
    if i - 2 >= 0:
        d[i] += d[i - 2]
    if i - 3 >= 0:
        d[i] += d[i - 3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(d[n])
