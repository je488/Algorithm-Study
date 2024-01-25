#0 ~ 9까지의 숫자를 k+1개 자리에 넣기(2 <= k <= 9이므로 k+1 <= 10)
#최대 10개의 수를 10개 자리에 넣기 -> 10! = 3628800, 1억보다 작으므로 모든 경우 다 해보기
#check는 사용 여부를 체크하는 리스트로 check[i]가 True면 i는 이미 사용한 수
#num은 만든 수를 저장하는 변수로 편리하게 숫자를 이어붙이기 위해 문자열 사용
#index == k+1이면 하나의 수를 만들었으므로 ok 함수를 이용하여 부등호 관계를 만족하는지 체크
#ok 함수에서 i번째와 i+1번째의 수는 i번째 부등호를 이용하여 비교
#ok 함수가 True를 리턴하면(부등호 관계를 만족하면) 최대값과 최소값을 출력하기 위해 ans에 저장
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def ok(num):
    for i in range(k):
        if a[i] == '<':
            if num[i] > num[i+1]:
                return False
        elif a[i] == '>':
            if num[i] < num[i+1]:
                return False
    return True

def go(index, num):
    if index == k+1:
        if ok(num):
            ans.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
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
