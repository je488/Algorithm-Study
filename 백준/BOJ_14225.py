#s의 크기는 n이고 n <= 20, s의 부분수열의 개수는 2^n(수열에 포함하거나 포함하지 않거나)
#2^20 = 1048576, 1억보다 작으므로 모든 부분수열 다 만들어보기
#수열을 이루고 있는 수 <= 10만, n <= 20이므로 모든 부분 수열의 합 <= 200만
#크기가 200만인 boolean 배열을 만들고 부분수열의 합으로 만들 수 있는지 없는지 체크
#c[i]값이 True이면 i는 부분수열의 합으로 만들 수 있는 수
#1부터 1씩 증가하며 만들 수 있는지 검사하다가 만들 수 없으면(c[i]값이 False이면) 그 수가 정답
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
c = [False] * n * 100000
def go(i, sum):
    if i == n:
        c[sum] = True
        return
    go(i+1, sum+s[i])
    go(i+1, sum)
go(0, 0)
i = 1
while True:
    if c[i] == False:
        break
    i += 1
print(i)
