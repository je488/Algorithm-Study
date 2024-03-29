#BOJ_9095_2.py에 같은 수를 두 번 이상 연속해서 사용할 수 없다는 조건 추가
#D[i][j] : i를 1, 2, 3의 합으로 나타내는 방법의 수, 마지막에 사용한 수는 j
#마지막 수가 1 : 앞에서 i-1을 만듦(마지막 수는 2, 3만 가능) -> D[i][1] = D[i-1][2] + D[i-1][3]
#마지막 수가 2 : 앞에서 i-2을 만듦(마지막 수는 1, 3만 가능) -> D[i][2] = D[i-2][1] + D[i-2][3]
#마지막 수가 3 : 앞에서 i-3을 만듦(마지막 수는 1, 2만 가능) -> D[i][3] = D[i-3][1] + D[i-3][2]
#정답은 D[n][1] + D[n][2] + D[n][3]
#가장 작은 크기의 문제는 각각 1, 2, 3만 사용한 경우로 d[1][1] = d[2][2] = d[3][3] = 1
#오버플로우를 방지하기 위해 d의 값을 구할 때마다 나머지 연산하기
#정답은 3개의 값의 합으로 (A + B)%C = (A%C + B%C) % C이므로 마지막에 한번 더 나머지 연산
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
limit = 100000
d = [[0] * 4 for _ in range(limit + 1)]
mod = 1000000009
for i in range(1, limit+1):
    if i-1 >= 0:
        d[i][1] = d[i-1][2] + d[i-1][3]
        if i == 1:
            d[i][1] = 1
    if i-2 >= 0:
        d[i][2] = d[i-2][1] + d[i-2][3]
        if i == 2:
            d[i][2] = 1
    if i-3 >= 0:
        d[i][3] = d[i-3][1] + d[i-3][2]
        if i == 3:
            d[i][3] = 1
    d[i][1] %= mod
    d[i][2] %= mod
    d[i][3] %= mod

T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(d[n]) % mod)
