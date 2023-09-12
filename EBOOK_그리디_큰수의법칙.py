#이것이 취업을 위한 코딩테스트다 - 94p
#cnt는 주어진 숫자 중 가장 큰 수를 더하는 횟수, res는 정답
#주어진 숫자들 중 가장 큰 숫자를 k번 더하고 두번째로 큰 숫자를 1번 더하는 연산을 반복
#길이가 k+1인 수열이 반복되는 것과 같음 -> m // (k+1)은 수열이 반복되는 횟수
#m // (k+1) * k은 가장 큰 수가 등장하는 횟수
#단, m이 k+1로 나누어떨어지지 않는 경우 가장 큰 숫자를 m % (k+1)만큼 추가로 더하기
#따라서 cnt = m // (k+1) * k + m % (k+1)
#두번째로 큰 숫자를 더하는 횟수는 m - cnt와 같음
#가장 큰 숫자와 두번째로 큰 숫자를 더하는 횟수를 각각 구해 숫자와 곱한 뒤 res에 누적
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, k = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
res, cnt = 0, 0
cnt += m // (k+1) * k
cnt += m % (k+1)
res += cnt * li[0]
res += (m - cnt) * li[1]
print(res)
