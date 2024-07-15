#연산자의 종류는 4가지, N-1개의 자리에 N-1개의 연산자가 올 수 있으므로 방법의 수는 O(4^(N-1))
#N-1 <= 10이므로 전체 경우의 수는 4^10 = 1048576(실제 경우의 수는 1048576보다 작음)
#ex) a = 3, b = 3, c = 2, d = 2인 경우
#ex) 10개의 위치 중 +가 올 수 있는 곳을 정하기(10C3) -> 7개의 위치가 남음
#ex) 7개의 위치 중 -가 올 수 있는 곳 정하기(7C3) -> 4개의 위치가 남음
#ex) 4개의 위치 중 *가 올 수 있는 곳 정하기(4C2) -> 2개의 위치가 남음
#ex) 자동으로 나머지 2개의 위치에 //가 오게 됨(2C2)
#ex) 경우의 수는 10! / 3!3!2!2! = 25200으로 1048576보다 작음
#1048576, 25200 모두 1억보다 작으므로 모든 방법 다 해보기(브루트 포스)
#index는 현재 계산해야 하는 인덱스
#cur는 index-1번째까지 계산한 결과
#plus, minus, mul, div는 사용할 수 있는 연산자의 개수
#index == len(a)이면 정답을 찾은 경우로 현재까지 구한 정답과 비교해서 최대값, 최소값 구하기
#1번 연산자와 a[1]부터 연산을 시작하므로 1번 연산자를 정하기 전까지의 결과는 a[0]
#따라서 처음에 함수 호출 시 index는 1, cur는 a[0]
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def calc(a, index, cur, plus, minus, mul, div):
    global max_res, min_res
    if index == len(a):
        max_res = max(cur, max_res)
        min_res = min(cur, min_res)
        return
    if plus > 0:
        calc(a, index+1, cur+a[index], plus-1, minus, mul, div)
    if minus > 0:
        calc(a, index+1, cur-a[index], plus, minus-1, mul, div)
    if mul > 0:
        calc(a, index+1, cur*a[index], plus, minus, mul-1, div)
    if div > 0:
        if cur >= 0:
            calc(a, index+1, cur//a[index], plus, minus, mul, div-1)
        else:
            calc(a, index+1, -(-cur//a[index]), plus, minus, mul, div+1)

n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
max_res = -int(1e9)
min_res = int(1e9)
calc(a, 1, a[0], plus, minus, mul, div)
print(max_res)
print(min_res)
