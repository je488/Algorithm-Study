#BOJ_2529_1.py는 k+1자리의 정수를 만든 후에 부등호를 만족하는지 체크
#따라서 6 < 5 > < <와 같이 중간에 이미 대소관계가 지켜지지 않은 경우에도 재귀 함수 호출
#시간을 단축시키기 위해 재귀 함수를 호출하기 전에 대소관계를 지키는지 체크
#good 함수는 두 숫자 x, y가 부등호 op의 관계인지 검사하여 맞으면 True, 틀리면 False 리턴
#따라서 이전에 사용하지 않았고 good 함수가 True를 리턴하는 경우에만 재귀 함수 호출
#index가 0이면 num이 비어있어 비교할 게 없으므로 good 함수의 리턴값과 상관없이 함수 호출
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def good(x, y, op):
    if op == '<':
        if x > y:
            return False
    if op == '>':
        if x < y:
            return False
    return True

def go(index, num):
    if index == k+1:
        ans.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
        if index == 0 or good(num[index-1], str(i), a[index-1]):
            check[i] = True
            go(index + 1, num + str(i))
            check[i] = False

k = int(input())
a = input().split()
ans = []
check = [False] * 10
go(0, '')
ans.sort()
print(ans[-1])
print(ans[0])
