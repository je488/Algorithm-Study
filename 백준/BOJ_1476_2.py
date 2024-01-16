#나머지를 이용하여 풀기
#모든 E, S, M에서 1씩 빼면 0 <= E < 15, 0 <= S < 28, 0 <= M < 19
#위의 범위는 각각 15, 28, 19로 나눈 나머지 값의 범위
#year를 0부터 1씩 증가시키면서 15, 28, 19로 나눈 나머지 값이 입력으로 주어진 E, S, M과 같은지 확인
#1씩 빼서 정답을 구했으므로 출력 시 year에 +1 해주기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
E, S, M = map(int, input().split())
E -= 1
S -= 1
M -= 1
year = 0
while True:
    if year % 15 == E and year % 28 == S and year % 19 == M:
        print(year + 1)
        break
    year += 1
