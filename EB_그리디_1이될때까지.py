#이것이 취업을 위한 코딩테스트다 - 101p
#k는 2 이상의 자연수이므로 1을 빼는 것보다 k로 나누는 것이 주어진 숫자를 빠르게 줄일 수 있음
#n이 k로 나누어 떨어질 때까지 1을 빼고 k로 나누기를 반복(단, n이 k보다 작으면 반복문 탈출)
#반복문을 탈출한 뒤 남아있는 수에 대하여 1씩 빼기
#target은 n을 k로 나누어 떨어질 수 있게 만든 수
#n - target은 n이 k로 나누어 떨어질 때까지 1을 빼야하는 횟수
#n = 25, k = 3인 경우, 반복문을 탈출했을 때 n = 0, res = 7
#n이 1이 될때까지만 수행하면 되므로 res에서 1을 빼서(-1을 더해서) 정답은 6
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
res = 0
while True:
    target = (n // k) * k
    res += (n - target)
    n = target
    if n < k:
        break
    res += 1
    n //= k
res += (n - 1)
print(res)
