#수의 개수가 가장 많은 경우는 1이 n개인 경우이므로 각각의 수가 최대 n개 올 수 있음
#각각의 수에는 1, 2, 3 총 3가지가 올 수 있으므로 전체 경우의 수는 3^n보다 작거나 같음
#n <= 10이므로 경우의 수는 최대 3^10 = 59049 -> 수가 크지 않으므로 모든 경우의 수 만들어보기
#go(s, goal)에서 s는 현재 함수의 호출 시점에서의 합
#반복문을 사용하여 각각 1, 2, 3을 사용하는 경우의 합 구하기
#s == goal인 경우 정답 1개를 찾았으므로 1 리턴
#s > goal인 경우 함수를 계속 호출해도 답을 구할 수 없으므로 0 리턴
#하나의 함수는 최대 3개의 함수를 호출하고 함수의 깊이는 최대 N이므로 시간 복잡도는 O(3^N)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def go(s, goal):
    if s > goal:
        return 0
    if s == goal:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(s + i, goal)
    return now
T = int(input())
for _ in range(T):
    n = int(input())
    print(go(0, n))
