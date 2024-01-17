#버튼을 누르는 횟수가 최소가 되어야 하므로 불필요한 값, 중복되는 값이 없어야 함
#따라서 숫자 버튼을 누르고 그 다음 +나 -중 하나만 연속해서 누르기
#이동할 채널 c를 정하고 고장난 버튼이 있는지 확인
#고장난 버튼이 포함되어 있지 않다면 |c - n|을 계산하여 +/- 버튼을 몇 번 눌러야 하는지 계산
#broken은 숫자 버튼의 고장 여부를 나타내는 리스트(고장났으면 True, 고장나지 않았으면 False)
#숫자 버튼을 누르지 않고 +/- 버튼만 눌러야 정답이 되는 경우도 있음
#ex) 현재 채널 : 100, N = 102 -> 정답 : 102 - 100 = 2
#따라서 숫자 버튼을 누르지 않는 경우(|n - 100|)를 정답의 초기값으로 설정
#반복문을 이용하여 0 ~ 1000000까지 이동할 채널 c를 결정하고 possible 함수로 이동가능한지 판단
#possible 함수는 채널 c로 이동 가능하면 c의 숫자 개수 리턴, 불가능하면 0 리턴
#c를 계속해서 10으로 나누면서 각 자리에 해당하는 숫자 버튼이 고장났는지 확인
#c = 0인 경우 0번이 고장났으면 0 리턴, 고장나지 않았으면 1 리턴
#채널 c로 이동 가능한 경우 c와 |c - n|을 더하여 실제로 버튼을 누르는 횟수 구하기
#버튼을 누르는 횟수가 이전에 구한 정답(ans)보다 작으면 ans값 바꿔주기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
m = int(input())
broken = [False] * 10
if m > 0:
    button = list(map(int, input().split()))
else:
    button = []
for b in button:
    broken[b] = True

def possible(c):
    if c == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if broken[c % 10]:
            return 0
        l += 1
        c //= 10
    return l

ans = abs(n-100)
for i in range(0, 1000001):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c - n)
        if ans > l + press:
            ans = l + press
print(ans)
