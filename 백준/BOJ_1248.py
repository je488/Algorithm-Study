#s가 하나의 문자열로 주어지므로 2차원 리스트(sign)로 변경
#sign[i][i]는 i번째 수의 부호
#따라서 sign[i][i]가 0보다 크면 1 ~ 10, 0보다 작으면 -10 ~ -1, 0이면 0을 ans[i]에 저장
#i번째 수를 결정하면 sign[j][i](0 <= j < i)꼴의 부호를 모두 검사할 수 있음
#따라서 수열을 만든 뒤에 부호가 맞는지 체크하지 않고 수를 하나씩 결정할 때 부호가 맞는지 체크
#check 함수는 index번째 수로 끝나는 모든 합(s)을 구해서 s의 부호가 입력과 같은 지 체크
#모든 합의 부호가 입력과 같으면 True, 다르면 False 리턴
#check 함수가 True를 리턴하면 재귀 함수(go)를 호출하고 False를 리턴하면 함수 호출 종료
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def check(index):
    s = 0
    for i in range(index, -1, -1):
        s += ans[i]
        if sign[i][index] == 0:
            if s != 0:
                return False
        elif sign[i][index] < 0:
            if s >= 0:
                return False
        elif sign[i][index] > 0:
            if s <= 0:
                return False
    return True

def go(index):
    if index == n:
        return True
    if sign[index][index] == 0:
        ans[index] = 0
        return check(index) and go(index+1)
    for i in range(1, 11):
        ans[index] = sign[index][index] * i
        if check(index) and go(index+1):
            return True
    return False

n = int(input())
s = input().rstrip()
sign = [[0] * n for _ in range(n)]
ans = [0] * n
cnt = 0
for i in range(n):
    for j in range(i, n):
        if s[cnt] == '0':
            sign[i][j] == 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1
go(0)
print(' '.join(map(str, ans)))
